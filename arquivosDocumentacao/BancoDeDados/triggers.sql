-- TRIGGERS PEDIDO
CREATE OR REPLACE TRIGGER trg_atualiza_pedido_qtdEstoque
BEFORE INSERT ON Pedido
FOR EACH ROW
DECLARE
    v_quantidade_lote NUMBER(10,2);
    v_loteID NUMBER;
    v_quantidade_lote_total NUMBER(10,2);
    quantidade_aux NUMBER := :NEW.Quantidade;
BEGIN
    SELECT SUM(QuantidadeRestante) INTO v_quantidade_lote_total
    FROM Lote
    WHERE ReceitaID = :NEW.ReceitaID
      AND DataValidade <= TRUNC(SYSDATE);
    IF v_quantidade_lote_total < :NEW.Quantidade THEN
            RAISE_APPLICATION_ERROR(-20001, 'Não há estoque suficiente.');
    END IF;
    
    LOOP
        SELECT QuantidadeRestante, LoteID INTO v_quantidade_lote, v_loteID
        FROM Lote
        WHERE ReceitaID = :NEW.ReceitaID
          AND DataValidade <= TRUNC(SYSDATE) AND
          QuantidadeRestante > 0
        ORDER BY DataProducao ASC FETCH FIRST 1 ROW ONLY;
        IF v_quantidade_lote < quantidade_aux THEN
            UPDATE Lote SET QuantidadeRestante = 0 Where loteID = v_loteID;
            quantidade_aux := quantidade_aux - v_quantidade_lote;
        ELSE
            UPDATE Lote SET QuantidadeRestante = QuantidadeRestante - quantidade_aux where LoteID = v_loteID;
            quantidade_aux := 0;
        END IF;
        IF quantidade_aux = 0 THEN
            EXIT;
        END IF;
    END LOOP;
END;

CREATE OR REPLACE TRIGGER trg_atualiza_valorVenda_pedido
    AFTER INSERT ON Pedido
    FOR EACH ROW
    DECLARE
        valorVenda_receita NUMBER(5,2);
    BEGIN
     SELECT ValorVenda INTO valorVenda_receita FROM Receita WHERE ReceitaID = :NEW.ReceitaID;
      UPDATE Pedido
      SET ValorVenda = valorVenda_receita
      WHERE PedidoID = :NEW.PedidoID;
    END;

--TRIGGERS LOTEESTOQUE

CREATE OR REPLACE TRIGGER trg_verifica_quantidade_restante
BEFORE INSERT ON LoteEstoque
FOR EACH ROW
DECLARE
    v_quantidade_restante NUMBER(10,2);
    receita NUMBER(10,2);
    quantidade_usada_receita NUMBER := -1;
    quantidade_produzida NUMBER;
    receita_id NUMBER;
    ingrediente_id NUMBER;
BEGIN
  BEGIN
    SELECT ReceitaID INTO receita_id From lote where loteID = :NEW.LoteID;
    SELECT ingredienteID INTO ingrediente_id FROM Estoque Where EstoqueID = :NEW.EstoqueID;
    SELECT DISTINCT rin.QuantidadeUsada INTO quantidade_usada_receita
    FROM
        ReceitaIngredientes rin
        INNER JOIN lote lot ON lot.ReceitaID = rin.ReceitaID    
    WHERE rin.ReceitaID = receita_id AND rin.IngredienteID = ingrediente_id FETCH FIRST ROW ONLY;
    EXCEPTION
    WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20001, 'Esta receita não usa este ingrediente.');
    END;
    SELECT QuantidadeProduzida INTO quantidade_produzida 
    FROM Lote WHERE LoteID = :NEW.LoteID;
    :NEW.QuantidadeUsada := quantidade_usada_receita * quantidade_produzida;
    SELECT QuantidadeRestante INTO v_quantidade_restante
    FROM Estoque
    WHERE EstoqueID = :NEW.EstoqueID;
    
    IF :NEW.QuantidadeUsada > v_quantidade_restante THEN
        RAISE_APPLICATION_ERROR(-20001, 'Quantidade usada maior que a quantidade restante no estoque.');
    ELSE
        UPDATE Estoque
        SET QuantidadeRestante = v_quantidade_restante - :NEW.QuantidadeUsada
        WHERE EstoqueID = :NEW.EstoqueID;
    END IF;
END;

-- TRIGGER LOTE
CREATE OR REPLACE TRIGGER trg_lote_alterarValorVenda_e_ValorProducao
    BEFORE UPDATE ON Lote
FOR EACH ROW
DECLARE
    v_venda_atual NUMBER(10,2);
    v_venda_lote NUMBER(10,2);
    v_prod_lote NUMBER(10,2);
    VP NUMBER (10,2);
    ML NUMBER(10,2);
    CF NUMBER(10,2);
    IMPOSTO NUMBER(10,2);
BEGIN
    IF :NEW.CadastroLoteEstoqueConcluido = 1 AND :OLD.CadastroLoteEstoqueConcluido = 0 THEN        
        
        --Calcula valor de producao:
        SELECT SUM(esl.QuantidadeUsada * (es.ValorCompra/es.QuantidadeComprada)) INTO v_prod_lote
        FROM
            LoteEstoque esl
            INNER JOIN Estoque es ON es.EstoqueID = esl.EstoqueID 
        WHERE
            esl.LoteID = :NEW.LoteID;
        :NEW.ValorProducao := v_prod_lote;
        -- Calcula novo valor de venda:
        SELECT ValorVenda INTO v_venda_atual 
        FROM
            Receita
        WHERE
            ReceitaID = :NEW.ReceitaID;
        SELECT ValorPorcentagem/100 into ML FROM CustosGerais WHERE Identificador = 'ML';
        SELECT ValorPorcentagem/100 into CF FROM CustosGerais WHERE Identificador = 'CF';
        SELECT ValorPorcentagem/100 into IMPOSTO FROM CustosGerais WHERE Identificador = 'IMPOSTO';
        ML := (:NEW.ValorProducao/:NEW.QuantidadeProduzida * ML);
        CF := CF * ML;
        IMPOSTO := IMPOSTO * ML;
        v_venda_lote := ML + CF + IMPOSTO;
        
        IF v_venda_lote > v_venda_atual THEN
            UPDATE Receita SET ValorVenda = v_venda_lote WHERE ReceitaID = :NEW.RECEITAID;
        END IF;
    END IF;
END;
