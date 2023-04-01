$(document).ready(function(){
    const cityDataBox= document.querySelector('cities-data-box');
console.log(cityDataBox);

$.ajax({
    type:'GET',
    url:'/cities-json/',
    success: function(response){
        console.log(response.data)
        const cityData = response.data
        cityData.map(item=>{
            const option=document.createElement("div")
            option.textContent = item.city_name
            option.setAttribute('class', 'item')
            option.setAttribute('value', item.name)
            cityDataBox.appendChild(option)
        })
    },
    error:function(error){
        console.log(error)
    }
})





})
