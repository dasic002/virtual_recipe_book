let recipeForm = document.querySelectorAll(".multiField")
let container = document.querySelector("#ingredient_form")
let addButton = document.querySelector("#add-form")
let removeButton = document.querySelectorAll(".remove-form")
let totalForms = document.querySelector("#id_ingredients_needed-TOTAL_FORMS")

let formNum = recipeForm.length - 1
addButton.addEventListener('click', addForm)

function addForm(e) {
    e.preventDefault()
    // copy form
    let newForm = recipeForm[0].cloneNode(true)
    let formRegex = RegExp(`ingredients_needed-(\\d){1}-`, 'g')
    
    // copy delete button
    // let newDeleteBtn = removeButton[0].cloneNode()
    // variable holding elements
    // let formWithButton = newForm
    // newForm = newForm.after(newDeleteBtn)

    formNum++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `ingredients_needed-${formNum}-`)
    container.appendChild(newForm)

    // newDeleteBtn.innerHTML = newDeleteBtn.innerHTML.replace(formRegex, `ingredients_needed-${formNum}-`)
    // container.appendChild(newDeleteBtn)

    totalForms.setAttribute('value', `${formNum + 1}`)
    console.log("Run the function!")
}