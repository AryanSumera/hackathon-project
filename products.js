function loadProducts(){

fetch(API+"/products")
.then(res=>res.json())
.then(data=>{

let table=document.getElementById("products")

table.innerHTML=""

data.forEach(p=>{

table.innerHTML+=`
<tr>
<td>${p[0]}</td>
<td>${p[1]}</td>
<td>${p[2]}</td>
<td>${p[3]}</td>
</tr>
`

})

})

}

function addProduct(){

let name=document.getElementById("name").value
let sku=document.getElementById("sku").value
let unit=document.getElementById("unit").value

fetch(API+"/products",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({name,sku,unit})

})

.then(()=>loadProducts())

}