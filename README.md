# gerador-lista
Sorteio de Pratos para o Café da Manhã

Este script Python automatiza o sorteio de pratos para um café da manhã coletivo, garantindo que cada item seja atribuído de forma justa entre os participantes. Ele é ideal para organizar eventos onde cada pessoa deve trazer um prato específico, evitando repetições excessivas e distribuindo a responsabilidade de forma equilibrada.
Como Funciona

O programa utiliza um dicionário pratos que armazena os nomes dos pratos e a quantidade de vezes que cada um pode ser sorteado (inicialmente 2 para a maioria, exceto pipoca que é 1). Os participantes inserem seus nomes e, em seguida, um prato disponível é sorteado aleatoriamente para eles. O script garante que nenhum prato seja sorteado mais vezes do que a quantidade definida.
Pré-requisitos

Para executar este script, você só precisa ter o Python 3 instalado em seu sistema.
Como Usar

    Salve o código: Copie o código fornecido e salve-o em um arquivo com extensão .py (por exemplo, sorteio_cafe.py).

    Execute o script: Abra um terminal ou prompt de comando, navegue até o diretório onde você salvou o arquivo e execute o comando:
    Bash

    python sorteio_cafe.py

    Insira os nomes: O programa solicitará que você digite o nome de cada participante. Após digitar o nome, pressione Enter.

    Atribuição do prato: O script sorteará automaticamente um prato para o participante e exibirá a mensagem informando qual prato a pessoa deve trazer.

    Encerrar o sorteio: Para finalizar a entrada de nomes e ver a lista final, digite 000 quando o programa solicitar um nome e pressione Enter.

Exemplo de Interação

Digite seu nome (ou "000" para encerrar): Ana
Ana, você deve trazer: Bolo
Digite seu nome (ou "000" para encerrar): Bruno
Bruno, você deve trazer: Salgados
Digite seu nome (ou "000" para encerrar): Carla
Carla, você deve trazer: Café
Digite seu nome (ou "000" para encerrar): 000

Lista final de participantes e seus pratos:
Ana: Bolo
Bruno: Salgados
Carla: Café

Personalização

Você pode facilmente personalizar a lista de pratos e a quantidade de vezes que cada um pode ser sorteado, editando o dicionário pratos no início do código:
Python

pratos = {
    'Nome do Prato 1': QuantidadeMaxima1,
    'Nome do Prato 2': QuantidadeMaxima2,
    # Adicione mais pratos aqui
}

Altere Nome do Prato para o nome desejado e QuantidadeMaxima para o número de vezes que aquele prato pode ser sorteado.
