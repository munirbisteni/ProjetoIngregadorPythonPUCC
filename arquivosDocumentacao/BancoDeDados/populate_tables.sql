 INSERT INTO CustosGerais (Descricao, ValorPorcentagem, identificador) VALUES ('Margem de lucro', 150.00, 'ML');
INSERT INTO CustosGerais (Descricao, ValorPorcentagem, identificador) VALUES ('Custo Fixo', 15.00, 'CF');
INSERT INTO CustosGerais (Descricao, ValorPorcentagem, identificador) VALUES ('Imposto', 12.00, 'IMPOSTO');

INSERT INTO Ingrediente (Nome, Alergenico, UnidadeID) VALUES ('Trigo', 1, 2);
INSERT INTO Ingrediente (Nome, Alergenico, UnidadeID) VALUES ('Ovo', 1, 3);
INSERT INTO Ingrediente (Nome, Alergenico, UnidadeID) VALUES ('Carne moída', 0, 2);
INSERT INTO Ingrediente (Nome, Alergenico, UnidadeID) VALUES ('Tomate', 0, 3);
INSERT INTO Ingrediente (Nome, Alergenico, UnidadeID) VALUES ('Alface', 0, 2);
INSERT INTO Ingrediente (Nome, Alergenico, UnidadeID) VALUES ('Milho', 0, 2);

INSERT INTO Receita (ValorVenda, Nome) VALUES (0,'Esfirra de tomate');
INSERT INTO Receita (ValorVenda, Nome) VALUES (0,'Esfirra de carne');
INSERT INTO Receita (ValorVenda, Nome) VALUES (0,'Esfirra de milho');
INSERT INTO Receita (ValorVenda, Nome) VALUES (0,'Pão sírio');

INSERT INTO ReceitaIngredientes (ReceitaID, IngredienteID, QuantidadeUsada) VALUES(1, 1, 100);
INSERT INTO ReceitaIngredientes (ReceitaID, IngredienteID, QuantidadeUsada) VALUES(1, 2, 1);
INSERT INTO ReceitaIngredientes (ReceitaID, IngredienteID, QuantidadeUsada) VALUES(1, 4, 1);


INSERT INTO ReceitaIngredientes (ReceitaID, IngredienteID, QuantidadeUsada) VALUES(2, 1, 100);
INSERT INTO ReceitaIngredientes (ReceitaID, IngredienteID, QuantidadeUsada) VALUES(2, 2, 1);
INSERT INTO ReceitaIngredientes (ReceitaID, IngredienteID, QuantidadeUsada) VALUES(2, 3, 200);

INSERT INTO ReceitaIngredientes (ReceitaID, IngredienteID, QuantidadeUsada) VALUES(3, 6, 100);
INSERT INTO ReceitaIngredientes (ReceitaID, IngredienteID, QuantidadeUsada) VALUES(3, 6, 1);
INSERT INTO ReceitaIngredientes (ReceitaID, IngredienteID, QuantidadeUsada) VALUES(3, 6, 200);

INSERT INTO Unidade (Descricao, identificador) VALUES ('Quilograma', 'KG');
INSERT INTO Unidade (Descricao, identificador) VALUES ('Grama', 'G');
INSERT INTO Unidade (Descricao, identificador) VALUES ('Unidade', 'UN');
INSERT INTO Unidade (Descricao, identificador) VALUES ('Litro', 'L');

INSERT INTO Estoque (IngredienteID, QuantidadeComprada, QuantidadeRestante, DataValidade, ValorCompra)
              VALUES( 1,            100000, 100000, TO_DATE('2024-05-15', 'YYYY-MM-DD'),  50000);
INSERT INTO Estoque (IngredienteID, QuantidadeComprada, QuantidadeRestante, DataValidade, ValorCompra)
              VALUES( 2,            1000, 1000, TO_DATE('2024-05-15', 'YYYY-MM-DD'),  700);
INSERT INTO Estoque (IngredienteID, QuantidadeComprada, QuantidadeRestante, DataValidade, ValorCompra)
              VALUES( 3,            100000, 100000, TO_DATE('2024-05-15', 'YYYY-MM-DD'),  50000);
INSERT INTO Estoque (IngredienteID, QuantidadeComprada, QuantidadeRestante, DataValidade, ValorCompra)
              VALUES( 5,            1000, 1000, TO_DATE('2024-05-15', 'YYYY-MM-DD'),  700);
INSERT INTO Estoque (IngredienteID, QuantidadeComprada, QuantidadeRestante, DataValidade, ValorCompra)
              VALUES( 4,            1000, 1000, TO_DATE('2024-05-15', 'YYYY-MM-DD'),  700);
     
INSERT INTO Lote (ReceitaID, DataProducao,DataValidade,QuantidadeProduzida,QuantidadeRestante) 
            VALUES(1, TO_DATE('2024-04-14', 'YYYY-MM-DD'),TO_DATE('2024-05-15', 'YYYY-MM-DD'), 100, 100); 
INSERT INTO LoteEstoque(LoteID, EstoqueID) VALUES(2, 5);
INSERT INTO LoteEstoque(LoteID, EstoqueID) VALUES(2, 1);
INSERT INTO LoteEstoque(LoteID, EstoqueID) VALUES(2, 2);

UPDATE Lote set lote.cadastroloteestoqueconcluido = 1 where loteID = 2;