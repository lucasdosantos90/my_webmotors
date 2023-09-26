addEventListener('DOMContentLoaded',()=>{
    const tune=document.getElementById('tune')
    const barra_lateral=document.getElementById('barra_lateral')
    const barra_lista=document.getElementById('barra_lista')
    const p_itens=[...document.getElementsByClassName('p_itens')]

    document.getElementById('form_id').reset()

    
    p_itens.map((itens)=>{
        itens.addEventListener('click',()=>{
            itens.nextElementSibling.click()
        })
    })


    tune.addEventListener('click',()=>{
        if((barra_lateral.style.display == 'none')){
            barra_lateral.style.display = 'block'
            barra_lista.style.position = 'absolute'
            barra_lista.style.paddingTop = '150px'
            barra_lista.style.top = '0px'
            barra_lista.style.left = '393px'
        }else if((barra_lateral.style.display !== 'none')){
            barra_lateral.style.display = 'none'
            barra_lista.style.position = 'absolute'
            barra_lista.style.paddingTop = '0px'
            barra_lista.style.top = '180px'
            barra_lista.style.left = '0px'
        }
    })
    
})