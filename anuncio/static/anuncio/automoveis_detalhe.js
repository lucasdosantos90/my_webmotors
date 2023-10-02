addEventListener('DOMContentLoaded',()=>{
    const automovel_fotos=[...document.getElementsByClassName('automovel_fotos')]
    let btn_img_left = [...document.getElementsByClassName('btn_img_left')]
    let btn_img_right = [...document.getElementsByClassName('btn_img_right')]
    automovel_fotos.map((auto_fotos)=>{
        auto_fotos.style.display = 'none'
        for (let index = 0; index <= 2; index++) {
            automovel_fotos[index].style.display = 'initial'
        }
        auto_fotos.addEventListener('click',()=>{
            auto_fotos.classList.toggle('img_full')
        })
    })
    let foto1=0
    let foto2=0
    let foto3=0
    btn_img_left.map((btn)=>{
        btn.addEventListener('click',(ev)=>{
            for (let index = 0; index < 5; index++) {
                automovel_fotos[index].style.display = 'none'
            }
            for (let index = 2; index < 5; index++) {
                automovel_fotos[index].style.display = 'initial'
            }
        })
    })
    btn_img_right.map((btn)=>{
        btn.addEventListener('click',(ev)=>{
            for (let index = 0; index < 5; index++) {
                automovel_fotos[index].style.display = 'none'
            }
            for (let index = 0; index < 3; index++) {
                automovel_fotos[index].style.display = 'initial'
            }
        })
    })
})