const submit=document.getElementById('submit');
const btns= document.querySelectorAll('.nav-btn');
const slides= document.querySelectorAll('.img-slide');
const search=document.querySelector('.searchbar2');
const searchicon=document.querySelector('.searchicon');

// searchicon.addEventListener('click',()=>{
//     search.style.display('block');
// })

// document.addEventListener('click',()=>{
//     search.style.display('none');
// })

var sliderNav=function(manual) {
    btns.forEach((btn)=>{
        btn.classList.remove('active');
    });
    
    slides.forEach((slide)=>{
        slide.classList.remove('active');
    });
    

    btns[manual].classList.add('active');
    slides[manual].classList.add('active');

};

btns.forEach((btn, i)=>{
    btn.addEventListener('click', ()=>{
        // console.log('clicked');
        sliderNav(i);
    });
});


document.addEventListener('DOMContentLoaded',function () {
    let currentIndex=0;

    function nextSlide() {
        currentIndex=(currentIndex+1)%slides.length;
        sliderNav(currentIndex);
        // updateSlider();
        
    };
    // function updateSlider() {
    //     const translateValue=-currentIndex*100;
        
    // };

    setInterval(nextSlide,10000)

    // updateSlider();
    
});

// Increasing and decreasing cartitem quantity
document.addEventListener("DOMContentLoaded", function() {
    const increaseButtons = document.querySelectorAll(".increase");
    const decreaseButtons = document.querySelectorAll(".decrease");
    const quantityValues = document.querySelectorAll(".quantity-value");
    const totalAmount = document.getElementById("total-amount");

    function updateTotal() {
        let total = 0;

        for (let i = 0; i < quantityValues.length; i++) {
            const quantity = parseInt(quantityValues[i].textContent);
            const price = parseFloat(quantityValues[i].closest("#cartitem").querySelector(".item-price").textContent);
            total += quantity * price;
        }

        totalAmount.textContent = total.toFixed(2);
    }

    increaseButtons.forEach((button, index) => {
        button.addEventListener("click", () => {
            let quantity = parseInt(quantityValues[index].textContent);
            quantityValues[index].textContent = quantity + 1;
            updateTotal();
        });
    });

    decreaseButtons.forEach((button, index) => {
        button.addEventListener("click", () => {
            let quantity = parseInt(quantityValues[index].textContent);
            if (quantity > 1) {
                quantityValues[index].textContent = quantity - 1;
                updateTotal();
            }
        });
    });

    // Initialize the total when the page loads
    updateTotal();
});


// Submit button functionalities

submit.addEventListener('submit',(event)=>{
    event.preventDefault;
    // const deactivate=document.querySelector('.cartBtn');
    // deactivate.style.background('light-gray');
});
