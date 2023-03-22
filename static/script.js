function updateVal(){
    sum = document.getElementById("sum").value;
    pr = document.getElementById("pr").value;
    term = document.getElementById("term").value;

    sumVal = document.getElementById("sumVal");
    prVal = document.getElementById("prVal");
    termVal = document.getElementById("termVal");

    sumVal.textContent = sum+"млн";
    prVal.textContent = pr+"%";
    termVal.textContent = term+"мес";
}