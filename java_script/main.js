filter = false // only allow the values containing D
visible = false
const things = ["James","Letty","Dominic","Torretto","Dan","luda chris","Joshua"]
var text=""

function load(){
    visible = !visible
    if(visible){
        text = "<ul>"
        things.forEach(print_elements)
        text+= "</ul>"
        document.getElementById("sample").innerHTML = text
    }else{
        document.getElementById("sample").innerHTML = "Hello javascript"
    }    
}

function toggle_filter(){
    filter = !filter
    if(filter){
        document.getElementById("status").innerHTML = "Currently showing records that contain letter D" 
    }else{
        document.getElementById("status").innerHTML = "Currently showing all records "
    }
    document.getElementById("btn").value = "set filter to "+!filter
    load()
}

function print_elements(value){
    if(filter){
        if (value.indexOf("d") != -1 || value.indexOf("D") != -1){
            text += "<li>"+value+"</li>"
        }
    }else{
    text += "<li>"+value+"</li>"
    }
}