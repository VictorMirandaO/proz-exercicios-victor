// proximo

function cumprimentar(){
    console.log("Boas-vindas ao JavaScript!");
}

cumprimentar();

function multiplicar(num1, num2){
    return (num1 * num2)
}

multiplicar(3, 7);

// função regular
function somar(a, b){
    return (a + b);
}

// função anônima
const adicionar = function(a, b){
    return (a + b);
}

const soma = function(a, b){
    return (a + b);
}

soma(5, 9);

// função anônima declarada de forma tradicional
const seguinteNum = function(n){
    return (n + 1);
}

// arrow function
const proximoNum = (n) => {
    return (n + 1);
}

const proximoNum2 = n => n + 1;