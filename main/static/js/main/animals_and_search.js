fetch('http://127.0.0.1:8000/api/get_animal_list/')
    .then(resp => resp.json())
    .then((data) => {
        for (let animal of data){
            let aAnimal = document.createElement('a')
            aAnimal.classList.add('filter__item')
            aAnimal.setAttribute('href', `http://127.0.0.1:8000/animal_products/${animal.id}`)
            aAnimal.innerHTML = `
                <div class="filter__item-img" style="background-image: url(${animal.image});">
                </div>
                <h3 class="filter__item-text">${animal.name}</h3>
            `
            document.querySelector('.filter__wrap').append(aAnimal)
        }
    })


const searchInput = document.getElementById('search')
    searchInput.addEventListener('input', getSearchResult)
const searchResult = document.querySelector('.search_result')

function getSearchResult () {
    if (searchInput.value.length > 2) {
        fetch(`http://127.0.0.1:8000/api/search_products/?search=${searchInput.value}`)
            .then(resp => resp.json())
            .then((data) => {
                searchResult.style.display = 'block'
                searchResult.innerHTML = ''
                for (let item of data) {
                    searchResult.innerHTML += `
                    <a href="http://127.0.0.1:8000/product_description/${item.id}" class="search__drop-down-item">
                    <div class="search__drop-down-item-img">
                    <img src="${item.image_preview}">
                    </div>
                    <p class="search__drop-down-item-title">${item.name}</p>
                    </a>
                    `
                }
                if (data.length === 0) {
                    searchResult.innerHTML = `<div class="search__drop-down-item">
                    <p class="search__drop-down-item-title">По вашему запросу ничего не найдено</p>
                    </div>`
                }
            })
    } else {
    searchResult.style.display = 'none'
    searchResult.innerHTML = ''
    }
}
