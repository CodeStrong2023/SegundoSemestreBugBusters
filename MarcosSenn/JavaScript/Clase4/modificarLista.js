let numeros = [1,2,3,4,5,6,7,8,9,10]

const multiplicar = (num) =>{
   return numeros.map((elemento)=>  elemento * num)
}

console.log(multiplicar(2))