const campoBusca = document.querySelector("#busca")
const cards = document.querySelectorAll("#lista-equipes")

campoBusca.addEventListener("input", () => {
    cards.forEach((card) => {
        const nomeCard = card.querySelector(h3)
        const textoNome = nomeCard.textContent.toLowerCase()

        const encontrou = textoNome.includes(nomeCard)

        if (encontrou) {
            cards.style.display = ""
        } else{
            cards.style.display = "none"
        }
    })
})
