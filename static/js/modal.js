const openButtons = document.querySelectorAll(".abrir-modal")

openButtons.forEach((button) => {
    button.addEventListener('click', () => {
        const modalID = button.getAttribute('data-modal');
        const modal = document.getElementById(modalID);

        modal.showModal()
    })
})

const closeButtons = document.querySelectorAll('.fechar-modal')

closeButtons.forEach((button) => {
    button.addEventListener('click', () => {
        const modalID = button.getAttribute('data-modal');
        const modal = document.getElementById(modalID);

        modal.close()
    })
})

const cancelButtons = document.querySelectorAll('.cancelar-modal')

cancelButtons.forEach((button) => {
    button.addEventListener('click', () => {
        const modalID = button.getAttribute('data-modal');
        const modal = document.getElementById(modalID);

        modal.close()
    })
})