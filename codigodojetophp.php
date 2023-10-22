<?php
session_start();
ob_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Recuperar os valores dos campos do formulário
    $Nome = $_POST["Nome"];
    $Sobrenome = $_POST["Sobrenome"];
    $email = $_POST["email"];
    $telefone = $_POST["telefone"];
    $datanascimento = $_POST["datanascimento"];
    $opinion = $_POST["opinion"];


    
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    // Validar o nome e sobrenome
    if (empty($Nome)) {
        $_SESSION['errors'][] = "<span style='color: red;'>Por favor, preencha o campo Nome.</span>";
    }

    $Sobrenome = $_POST['Sobrenome'];
    if (empty($Sobrenome)) {
        $_SESSION['errors'][] = "<span style='color: red;'>Por favor, preencha o campo Sobrenome.</span>";
    }

    // Validar o email
    if (empty($email)) {
        $_SESSION['errors'][] = "<span style='color: red;'>Por favor, preencha o campo Email.</span>";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $_SESSION['errors'][] = "<span style='color: red;'>Formato de email inválido.</span>";
    }

    // Validar o telefone
    if (empty($telefone)) {
        $_SESSION['errors'][] = "<span style='color: red;'>Por favor, preencha o campo Telefone.</span>";
    } elseif (!preg_match("/^\d{2}\ \d{5}\d{4}$/", $telefone)) {
        $_SESSION['errors'][] = "<span style='color: red;'>Formato de telefone inválido. Use XX XXXXXXXXX.</span><br>";
    }
    // Valida a data de nascimento
      if (empty($datanascimento)) {
        $_SESSION['errors'][] = "<span style='color: red;'>Por favor, preencha o campo Data de Nascimento.</span>";
    } else {
        // Calcular a idade com base na data de nascimento
        $data_nascimento = new DateTime($datanascimento);
        $data_atual = new DateTime();
        $idade = $data_atual->diff($data_nascimento)->y;

        // Definir o limite de idade (por exemplo, 18 anos)
        $limite_idade = 18;

        // Verificar se a idade é menor que o limite
        if ($idade < $limite_idade) {
            $_SESSION['errors'][] = "<span style='color: red;'>Você deve ter pelo menos $limite_idade anos para prosseguir.</span>";
        }
        // Valida o campo opinião
        if (empty($opinion)) {
        $_SESSION['errors'][] = "<span style='color: red;'>Por favor, preencha o campo Opnião.</span>";
    }

    }
}
if (empty($_SESSION['errors'])) {
    // Redirecionar para a página de exibição dos dados
    header("Location: ConfirmarDados.php?Nome=" . urlencode($Nome) . "&Sobrenome=" . urlencode($Sobrenome) . "&email=" . urlencode($email) . "&telefone=" . urlencode($telefone) . "&idade=" . urlencode($idade) . "&opinion=" . urlencode($opinion));    exit; // Certifique-se de sair para evitar que o restante do código seja executado
} 

}
?>