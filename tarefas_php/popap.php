<?php

// Configurações do banco de dados
$servername = "localhost";
$username = "seu_usuario";
$password = "sua_senha";
$dbname = "medicamento_controle";

// Cria a conexão com o banco de dados
$conn = new mysqli($servername, $username, $password, $dbname);

// Verifica se ocorreu algum erro na conexão
if ($conn->connect_error) {
    die("Falha na conexão com o banco de dados: " . $conn->connect_error);
}

// Consulta para recuperar os dados do medicamento
$sql = "SELECT quantidade, validade FROM medicamento";
$result = $conn->query($sql);

// Verifica se a consulta retornou resultados
if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    
    // Obtém os valores do banco de dados
    $quantidadeEstoque = $row["quantidade"];
    $validade = new DateTime($row["validade"]);

    // Chama a função para calcular a venda diária
    $vendaDiaria = calcularVendaDiaria($quantidadeEstoque, $validade);
    
    // Calcula a quantidade total a ser vendida
    $diasRestantes = $validade->diff(new DateTime())->days;
    $quantidadeTotal = $vendaDiaria * $diasRestantes;

    // Exibe a notificação
    echo "Você precisa vender " . number_format($quantidadeTotal, 2) . " remédios em $diasRestantes dias.";
} else {
    echo "Nenhum medicamento encontrado no banco de dados.";
}

// Fecha a conexão com o banco de dados
$conn->close();

function calcularVendaDiaria($quantidadeAtual, $validade) {
    // Obter a data atual
    $dataAtual = new DateTime();
    $dataAtual->setTime(0, 0, 0);

    // Calcular a quantidade de dias restantes até a validade
    $diasRestantes = $validade->diff($dataAtual)->days;

    // Calcular a quantidade de remédios a serem vendidos por dia
    $vendaDiaria = $quantidadeAtual / $diasRestantes;

    return $vendaDiaria;
}

?>

