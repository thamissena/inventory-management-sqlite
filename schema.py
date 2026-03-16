#stringSQL:(Banco de dados SQL)
comandoSQL = {
	0: """
	CREATE TABLE IF NOT EXISTS Produtos (
		produtoID INTEGER PRIMARY KEY AUTOINCREMENT,
		produtoNome VARCHAR (200) NOT NULL,
		descricao VARCHAR (250) NOT NULL,
		precoProduto DECIMAL (9,2)  NOT NULL,
		qt INTEGER,
		CHECK (qt >0)
	);
	""",
	1: """
	CREATE TABLE IF NOT EXISTS Vendas (
		vendaID INTEGER PRIMARY KEY AUTOINCREMENT,
		produtoID INTEGER NOT NULL,
		qtVenda INTEGER NOT NULL,
		data date 
		CHECK (qtVenda >0), 
		FOREIGN KEY (produtoID) REFERENCES Produtos(produtoID)
	);
	""",
	2: """
	INSERT INTO Produtos (
		produtoNome,
		descricao,
		precoProduto,
		qt
	) VALUES (?, ?, ?, ?);
	""",
    3: """
	SELECT * FROM Produtos
	""",
	4: """ 
	SELECT qt  FROM Produtos WHERE produtoID = ?
    """,
    5: """
	INSERT INTO Vendas (
		produtoID,
		qtVenda,
		data
	) VALUES (?,?,?);
	""",
    6: """
	UPDATE  Produtos SET qt = qt - ?
	WHERE produtoID = ?
	""",
	7: """
	UPDATE  Produtos SET produtoNome = ?
	WHERE produtoID = ?
	""",
    8: """
	UPDATE Produtos SET descricao = ?
	WHERE produtoID = ?
	""",
    9: """
	UPDATE Produtos SET precoProduto = ?
	WHERE produtoID = ?
	""",
    10: """
	UPDATE Produtos SET qt = ?
	WHERE produtoID = ?
	""",
	11:""" 
	SELECT p.produtoID, p.produtoNome, p.descricao, p.precoProduto,p.qt, v.qtVenda, v.data
    FROM Produtos p LEFT JOIN Vendas v ON p.produtoID = v.produtoID

	""",
}

