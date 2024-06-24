
document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("search");
    const searchBtn = document.querySelector(".search-btn");
    const searchInput2 = document.getElementById("search2");
    const searchBtn2 = document.querySelector(".search2-btn");
    const products = document.querySelectorAll("#item-con");
    const searchbar2=document.querySelector('.searchbar2');
    const searchicon=document.querySelector('.searchicon');

    searchBtn.addEventListener("click", function(event) {
        event.preventDefault();
        const searchTerm = searchInput.value.toLowerCase();
        console.log(searchTerm);

        products.forEach(product => {
            const title = product.querySelector(".product-name").textContent.toLowerCase();
            if (title.includes(searchTerm)) {
                product.style.display = "block";
            } else {
                product.style.display = "none";
            }
        });
    });

    searchInput.addEventListener('focus',()=>{
        window.location.href='/search/'
    });

    searchBtn2.addEventListener("click", function(event) {
        event.preventDefault();
        const searchTerm2 = searchInput2.value.toLowerCase();
        // console.log(searchTerm);

        products.forEach(product => {
            const title = product.querySelector(".product-name").textContent.toLowerCase();
            if (title.includes(searchTerm2)) {
                product.style.display = "block";
            } else {
                product.style.display = "none";
            }
        });
    });

    searchInput2.addEventListener('focus',()=>{
        window.location.href='/search/'
        
    });

    document.addEventListener('keyup',(event)=>{
        if (event.key==='Enter') {
            if (window.innerWidth>=1000) {
                searchBtn.click();
                
            } else {
            searchBtn2.click();

            };
            
        };
    });


    // searchIcon display and navigation

    searchicon.addEventListener('click',()=>{
        const display= searchbar2.style.display='flex';
    })
});

