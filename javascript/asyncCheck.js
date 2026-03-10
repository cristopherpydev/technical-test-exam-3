/* llamadas asincronas */

// Implementa una función que:

// Simule una llamada asíncrona (Promise)
// Devuelva "OK" tras 1 segundo si un parámetro es true
// Lance un error si el parámetro es false
// Use async/await y try/catch


function peticion_asincrona(parametro){
    if(parametro == true){
        try {
        return new Promise((resolve) => {
        setTimeout(() => {
        resolve("OK");
        }, 1000);
        }
    );
    
        } catch (error){
        console.log("Ha habido un error inesperado.")    
        }
    return
}
}

async function llamada_asincrona() {
  console.log("Llamada a la petición");
  const result = await peticion_asincrona();
  console.log(result);
}

llamada_asincrona();
