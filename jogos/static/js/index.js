const campoBusca = document.querySelector("#busca")
const cards = document.querySelectorAll(".card")

campoBusca.addEventListener("input", () => {
    const texto = campoBusca.value.toLowerCase()

    cards.forEach((card) => {
        const tituloCard = card.querySelector("h3")
        const textoTitulo = tituloCard.textContent.toLowerCase()

        const encontrou = textoTitulo.includes(texto)

        if (encontrou) {
            card.style.display = ""
        } else {
            card.style.display = "none"
        }

        
    })
})