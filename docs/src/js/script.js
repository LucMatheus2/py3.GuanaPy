/**
 * A função ao qual resgata do banco de dados JSON os dados para formar a lista.
 * @param {Number} indice O indice de inicio para iniciar a lista 
 */ 
function filtrarLista(indice) {
    fetch("src/db/src_py3.json")
    .then(
        (response) => response.json()
        .then(
            (response) => 
            {
                console.log(response)
            }
        )
        .catch((exception) => 
        {
            alert("Deu ruim");
            console.log(exception);
        })
    )
    .catch
    (
        (exception) => 
        {
            alert("Deu ruim no inicio");
            console.log(exception)
        }
    );
}
/**
 * Função automática
 */
function autoload() {
    filtrarLista(1);
}
addEventListener("load",autoload);