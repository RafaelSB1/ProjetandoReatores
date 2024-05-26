let myChart;
export function criarGrafico1V(Y, X, legendaY, texto_eixoY, texto_eixoX, titulo, id) {
    const ctx = document.getElementById(id).getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
        datasets: [
            {
            label: legendaY,
            data: Y,
            parsing: {
                yAxisKey: legendaY,
            },
            },
        ],
        },
        options: {
            maintainAspectRatio: false,
            plugins: {
                title: {
                display: true,
                text: titulo,
                },
            },
            scales: {
                x: {
                type: 'category',
                labels: X, // Especifique os rótulos de categoria para o eixo x
                title: {
                    display: true,
                    text: texto_eixoX,
                },
                },
                y: {
                title: {
                    display: true,
                    text: texto_eixoY,
                },
                },
            },
            layout: {
                padding: 20,
            },
        },
    });
};

export function criarGrafico2V(Y1, Y2, X, legendaY1,legendaY2, texto_eixoY, texto_eixoX, titulo, id) {
    const ctx = document.getElementById(id).getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
        datasets: [
            {
            label: legendaY1,
            data: Y1,
            parsing: {
                yAxisKey: legendaY1, // Coloque a chave correta aqui, se necessário
            },
            },
            {
                label: legendaY2,
                data: Y2,
                parsing: {
                    yAxisKey: legendaY2, // Coloque a chave correta aqui, se necessário
                },
            },
        ],
        },
        options: {
            maintainAspectRatio: false,
            plugins: {
                title: {
                display: true,
                text: titulo,
                },
            },
            scales: {
                x: {
                type: 'category',
                labels: X, // Especifique os rótulos de categoria para o eixo x
                title: {
                    display: true,
                    text: texto_eixoX,
                },
                },
                y: {
                title: {
                    display: true,
                    text: texto_eixoY,
                },
                },
            },
            layout: {
                padding: 20,
            },
        },
    });
};

export function criarGrafico3V(Y1, Y2, Y3, X, legendaY1, legendaY2, legendaY3, texto_eixoY, texto_eixoX, titulo, id) {
    const ctx = document.getElementById(id).getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            datasets: [
                {
                label: legendaY1,
                data: Y1,
                parsing: {
                    yAxisKey: legendaY1, // Coloque a chave correta aqui, se necessário
                },
                },
                {
                    label: legendaY2,
                    data: Y2,
                    parsing: {
                        yAxisKey: legendaY2, // Coloque a chave correta aqui, se necessário
                    },
                },
                {
                    label: legendaY3,
                    data: Y3,
                    parsing: {
                        yAxisKey: legendaY3, // Coloque a chave correta aqui, se necessário
                    },
                },
            ],
        },
        options: {
            maintainAspectRatio: false,
            plugins: {
                title: {
                display: true,
                text: titulo,
                },
            },
            scales: {
                x: {
                type: 'category',
                labels: X, // Especifique os rótulos de categoria para o eixo x
                title: {
                    display: true,
                    text: texto_eixoX,
                },
                },
                y: {
                title: {
                    display: true,
                    text: texto_eixoY,
                },
                },
            },
        },
    });
};

export function criarGrafico4V(Y1, Y2, Y3, Y4, X, legendaY1, legendaY2, legendaY3, legendaY4, texto_eixoY, texto_eixoX, titulo, id) {
    const ctx = document.getElementById(id).getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
        datasets: [
            {
            label: legendaY1, //legenda
            data: Y1,
            parsing: {
                yAxisKey: legendaY1,
            },
            },
            {
                label: legendaY2,
                data: Y2,
                parsing: {
                    yAxisKey: legendaY2, 
                },
            },
            {
                label: legendaY3,
                data: Y3,
                parsing: {
                    yAxisKey: legendaY3, 
                },
            },
            {
                label: legendaY4,
                data: Y4,
                parsing: {
                    yAxisKey: legendaY4, 
                },
            },
        ],
        },
        options: {
            maintainAspectRatio: false,
            plugins: {
                title: {
                display: true,
                text: titulo,
                },
            },
            scales: {
                x: {
                type: 'category',
                labels: X, // Especifique os rótulos de categoria para o eixo x
                title: {
                    display: true,
                    text: texto_eixoX,
                },
                },
                y: {
                title: {
                    display: true,
                    text: texto_eixoY,
                },
                },
            },
            layout: {
                padding: 20,
            },
        },
        
    });
};

export function criarGraficoDTR(Y1, Y2, X1, X2, valorR_quadrado, legendaY1, legendaY2, texto_eixoY, texto_eixoX, titulo, id) {
    const ctx = document.getElementById(id).getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            datasets: [
                {
                    label: legendaY1,
                    data: Y1.map((value, index) => ({ x: X1[index], y: value })), // Convertendo para o formato de dados de dispersão
                    type: 'line',
                },
                {
                    label: legendaY2,
                    data: Y2.map((value, index) => ({ x: X2[index], y: value })), // Convertendo para o formato de dados de dispersão
                    pointBackgroundColor: 'rgba(150, 0, 50, 1)', // Cor dos pontos para a segunda série de dados
                    pointBorderColor: 'rgba(0, 0, 0, 1)',
                    type: 'scatter',
                    pointRadius: 5
                },
            ],
        },
        options: {
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: titulo,
                },
                subtitle: {
                    display: true,
                    text: `R² = ${valorR_quadrado}`,
                },
            }, 
            scales: {
                x: {
                    type: 'linear',
                    title: {
                        display: true,
                        text: texto_eixoX,
                    },
                },
                y: {
                    title: {
                        display: true,
                        text: texto_eixoY,
                    },
                },
            },
            layout: {
                padding: 20,
            },
        },
    });
};


const resultadosArray = [];
const contadorResultado = [];
const resultadosEE = [];
export function criarEstrutura(data, unidade) {
    const propriedade = Object.keys(data);
    
    //pega o tamanho do array da primeira propriedade (propriedade[0] - totadas devem ter o mesmo tamanho) e subtrai 1, pois o index começa do 0
    const tamanho = Object.keys(data).length //tamanho do vetor - número de propriedades
    let novaEstrutura = `
        <div class="card text-center mx-3 my-1">
        <h5 class="card-header px-5">Resultado ${contadorResultado.length+1}</h5>
        <div class="card-body">`;
    //loop que percorre o ultimo valor de cada array (vetor) e exibe no bloco de Resultados
    for (let i = 0; i < tamanho; i++) {
        if (propriedade[i] != "sucesso") {
            let ultimoIndex = data[propriedade[i]].length - 1
            novaEstrutura += `<h6>${propriedade[i]} = ${data[propriedade[i]][ultimoIndex]} ${unidade[i]}</h6>`; 
        }
    }; 
    novaEstrutura+=`
        </div>
        </div>  
    `;
    contadorResultado.push(1);
    resultadosArray.push(novaEstrutura); // Adicione a nova estrutura ao array
    if (resultadosArray.length > 3) {
        resultadosArray.shift(); // Se o tamanho for maior que 3, remova a estrutura mais antiga
    }
    // Atualize o conteúdo do elemento cardResultados com base nas estruturas no array
    document.getElementById("cardResultados").innerHTML = resultadosArray.join("");
};

export function modificarEstruturaEE(data,unidade) {
    let novaEstrutura = `
        <div class="card text-center mx-3 my-1">
        <h5 class="card-header px-5">Resultado ${contadorResultado.length+1}</h5>
        <div class="card-body">
        </div>
        </div>`;
    document.getElementById("cardResultados").innerHTML= novaEstrutura;

    let respostas = document.getElementsByClassName("card-body");
    let resposta = respostas[respostas.length-1];
    resposta.innerHTML = "Tabela de pontos de operação"
    var headers = Object.keys(data);
    var table = document.createElement("table");// Criar a tabela HTML  
    table.classList.add("table", "table-hover","m-2")
    var headerRow = table.insertRow(0);// Criar a linha do cabeçalho
    // Preencher o cabeçalho com as chaves do dicionário
    let contadorUnidade = 0;
    headers.forEach(function (header) {
      var th = document.createElement("th");
      th.textContent = header+unidade[contadorUnidade];
      headerRow.appendChild(th);
      contadorUnidade += 1;
    });
    // Preencher a tabela com os dados do dicionário
    for (var i = 0; i < data[headers[0]].length; i++) {
      var row = table.insertRow(i + 1);
      headers.forEach(function (header) {
        var cell = row.insertCell();
        cell.textContent = data[header][i];
      });
    }
    // Adicionar a tabela ao corpo do documento
    resposta.appendChild(table);
    novaEstrutura = document.getElementsByClassName("card")[respostas.length-1].outerHTML;

    contadorResultado.push(1);
    resultadosEE.push(novaEstrutura); // Adicione a nova estrutura ao array
    if (resultadosEE.length > 3) {
        resultadosEE.shift(); // Se o tamanho for maior que 3, remova a estrutura mais antiga
    }
    // Atualize o conteúdo do elemento cardResultados com base nas estruturas no array
    document.getElementById("cardResultados").innerHTML = resultadosEE.join("");
}

function subscrito() {
    const elementosComNome = document.getElementsByClassName("col-form-label");
        for (let i = 0; i < elementosComNome.length; i++) {
        let nome = elementosComNome[i].textContent;
        if (nome[0] === "U") {
            //A função não faz nada
        } else if (nome[0] === "Δ") {
            elementosComNome[i].innerHTML = `${nome.slice(0,2)}`+`<sub>${nome.slice(2)}</sub>`;
        } else if (nome === "taxa") {
        } else if (nome === "C(t)") {
        } else {
            elementosComNome[i].innerHTML = `${nome[0]}`+`<sub>${nome.slice(1)}</sub>`;
        }
    }
}

window.onload = subscrito;

function checkScreenSize() {
    // Verifique a largura da janela do navegador
    const windowWidth = window.innerWidth;
    // Se a largura for menor que um valor específico (por exemplo, 768 pixels),
    // adicione a classe navbar-nav-scroll ao elemento com o ID sidebar
    const sidebar = document.getElementById("sidebar");
    const main = document.getElementsByTagName("main")[0];
    if (windowWidth < 768) {
        sidebar.classList.add("navbar-nav-scroll");
    } else {
        // Caso contrário, remova a classe navbar-nav-scroll
        sidebar.classList.remove("navbar-nav-scroll");
        sidebar.classList.remove("d-none");
        main.classList.remove("d-none");
    }
}
// Execute a função quando a página for carregada e quando a janela for redimensionada
//window.addEventListener("load", checkScreenSize);
//window.addEventListener("resize", checkScreenSize);

$(function () {
    function checkScreenSize1() {
    if ($(window).width() <= 767) {
        // Tela pequena: mostra o popover para baixo
        $('#lista-de-simbolos').popover({
        placement: 'bottom'
        });
    } else {
        // Tela normal: mostra o popover para a direita
        $('#lista-de-simbolos').popover({
        placement: 'right'
        });
    }
    }

    // Ativa a função ao carregar e redimensionar a tela
    checkScreenSize1();
    $(window).resize(checkScreenSize1);
});

$(document).ready(function() {
    $('#botao').click(function() {
      // Armazenar o valor original do botão
      var valorOriginal = $(this).val();

      // Adicionar o spinner ao botão
      $(this).val('Ação em andamento...').prop('disabled', true);
      $('#errors-container').html('<div class="spinner-border" role="status"></div>')

      // Simular uma ação demorada (pode ser substituída por sua lógica real)
      setTimeout(function() {
        // Remover o spinner e restaurar o valor original do botão
        $('#botao').val(valorOriginal).prop('disabled', false);
      }, 2000); // Tempo de simulação (em milissegundos)
    });
});


 
