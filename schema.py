instructions = [
    "SET FOREIGN_KEY_CHECKS=0;",
    "DROP TABLE IF EXISTS prueba.user;",
    "DROP TABLE IF EXISTS prueba.market;",
    "SET FOREIGN_KEY_CHECKS=1;",
    """
        CREATE TABLE prueba.user (
            id INT PRIMARY KEY AUTO_INCREMENT, 
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL
            )
    """,
    """
        CREATE TABLE prueba.market (
            id INT PRIMARY KEY AUTO_INCREMENT,
            created_by INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT "0",
            FOREIGN KEY (created_by) REFERENCES user (id)
        )
    """,
]