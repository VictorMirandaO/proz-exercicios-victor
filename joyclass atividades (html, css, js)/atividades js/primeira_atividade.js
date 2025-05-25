// X é par e menor que 50
// X é menor que 50
// X é maior que 50

const numerosDaSorte = [37, 14, 26, 5, 94, 87];

numerosDaSorte.forEach(numero => {
    const ehPar = numero % 2 === 0;

    if (ehPar && numero < 50) {
        console.log(`${numero} é par e menor que 50`);
    } else if (numero < 50) {
        console.log(`${numero} é menor que 50`);
    } else if (numero > 50) {
        console.log(`${numero} é maior que 50`);
    }
});