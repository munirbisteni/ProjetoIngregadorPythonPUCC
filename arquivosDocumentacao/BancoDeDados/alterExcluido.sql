ALTER TABLE Cidade
ADD excluido NUMBER(1);
ALTER TABLE Cidade
ADD data_exclusao DATE;

ALTER TABLE Estado
ADD excluido NUMBER(1);
ALTER TABLE Estado
ADD data_exclusao DATE;

ALTER TABLE Estoque
ADD excluido NUMBER(1);
ALTER TABLE Estoque
ADD  data_exclusao DATE;

ALTER TABLE Ingrediente
ADD excluido NUMBER(1);
ALTER TABLE Ingrediente
ADD data_exclusao DATE;

ALTER TABLE Lote
ADD excluido NUMBER(1);
ALTER TABLE Lote
ADD data_exclusao DATE;

ALTER TABLE LoteEstoque
ADD excluido NUMBER(1);
ALTER TABLE LoteEstoque
ADD data_exclusao DATE;

ALTER TABLE Pedido
ADD excluido NUMBER(1);
ALTER TABLE Pedido
ADD data_exclusao DATE;

ALTER TABLE Receita
ADD excluido NUMBER(1);
ALTER TABLE Receita
ADD data_exclusao DATE;

ALTER TABLE ReceitaIngredientes
ADD excluido NUMBER(1);
ALTER TABLE ReceitaIngredientes
ADD data_exclusao DATE;

ALTER TABLE Unidade
ADD excluido NUMBER(1);
ALTER TABLE Unidade
ADD data_exclusao DATE;

ALTER TABLE Usuario
ADD excluido NUMBER(1);
ALTER TABLE Usuario
ADD data_exclusao DATE;

ALTER TABLE UsuarioRoles
ADD excluido NUMBER(1);
ALTER TABLE UsuarioRoles
ADD data_exclusao DATE;

ALTER TABLE Venda
ADD excluido NUMBER(1);
ALTER TABLE Venda
ADD data_exclusao DATE;


ALTER TABLE Venda MODIFY excluido DEFAULT 0;
ALTER TABLE UsuarioRoles MODIFY excluido DEFAULT 0;
ALTER TABLE Usuario MODIFY excluido DEFAULT 0;
ALTER TABLE Unidade MODIFY excluido DEFAULT 0;
ALTER TABLE ReceitaIngredientes MODIFY excluido DEFAULT 0;
ALTER TABLE Receita MODIFY excluido DEFAULT 0;
ALTER TABLE Pedido MODIFY excluido DEFAULT 0;
ALTER TABLE LoteEstoque MODIFY excluido DEFAULT 0;
ALTER TABLE Lote MODIFY excluido DEFAULT 0;
ALTER TABLE Ingrediente MODIFY excluido DEFAULT 0;
ALTER TABLE Estoque MODIFY excluido DEFAULT 0;
ALTER TABLE Estado MODIFY excluido DEFAULT 0;


update unidade set Excluido = 0;
update receitaIngredientes set Excluido = 0;
update Receita set Excluido = 0;
update Lote set Excluido = 0;
update LoteEstoque set Excluido = 0;
update ingrediente set Excluido = 0;
update estoque set Excluido = 0;
