describe venda

CREATE SEQUENCE StatusVenda_seq START WITH 1 INCREMENT BY 1 NOCACHE NOCYCLE;

create table StatusVenda(
      StatusVendaID NUMBER DEFAULT StatusVenda_seq.NEXTVAL PRIMARY KEY NOT NULL,
      Descricao VARCHAR2(255) not null,
      Identificador VARCHAR2(50) not null 
)

ALTER TABLE venda
ADD StatusVendaID NUMBER;

ALTER TABLE venda
ADD CONSTRAINT fk_status_venda
FOREIGN KEY (StatusVendaID)
REFERENCES StatusVenda(StatusVendaID);

insert into StatusVenda(descricao, identificador) values ('Venda cancelada','CANCELADA');
insert into StatusVenda(descricao, identificador) values ('Venda concluida','CONCLUIDA');
insert into StatusVenda(descricao, identificador) values ('Pedido em preparo','PREPARO');
insert into StatusVenda(descricao, identificador) values ('Pedido na fila (aberto)','ABERTO');
insert into StatusVenda(descricao, identificador) values ('Cancelado pelo estabelecimento', 'CANCL_INTERNO');