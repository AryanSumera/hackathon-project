function addReceipt(){

let product_id=document.getElementById("product_id").value
let warehouse_id=document.getElementById("warehouse_id").value
let quantity=document.getElementById("quantity").value

fetch(API+"/receipts",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
product_id,
warehouse_id,
quantity
})

})

.then(()=>alert("Receipt Added"))

}