
const lastCard = document.querySelector('.lastCard')
const stack = document.querySelector("main .stack");  
const cards = Array.from(stack.children)  
    .filter((child) => child.classList.contains("card"));  

// إعادة ترتيب البطاقات بحيث تكون الأخيرة في الأعلى  
cards.reverse().forEach((card) => stack.appendChild(card));  

function moveCard() {  
    const lastCard = stack.lastElementChild;  
    if (lastCard && lastCard.classList.contains("card")) {  
        lastCard.classList.add("swap");  

        setTimeout(() => {  
            lastCard.classList.remove("swap");  
            stack.insertBefore(lastCard, stack.firstElementChild);  
        }, 1200);  
    }  
}  

// تشغيل السلايدر تلقائيًا كل 4 ثوانٍ  
let autoplayInterval = setInterval(moveCard, 4000);  

// إضافة حدث النقر على البطاقات  
stack.addEventListener("click", function (e) {  
    const card = e.target.closest(".card");  
    if (card && card === stack.lastElementChild) {  
        card.classList.add("swap");  

        setTimeout(() => {  
            card.classList.remove("swap");  
            stack.insertBefore(card, stack.firstElementChild);  
        }, 1200);  
    }  
});