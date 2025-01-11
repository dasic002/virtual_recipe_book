let recipeForm = document.querySelectorAll(".multiField");
let container = document.querySelector("#ingredients_form");
let addBtn = document.querySelector("#add-form");
let removeBtns = document.querySelectorAll(".remove-form");
let totalForms = document.querySelector("#id_ingredients_needed-TOTAL_FORMS");

let formNum = recipeForm.length - 1;


addBtn.addEventListener('click', addForm);

container.onload = renderRemBtns();


function addForm(e) {
    e.preventDefault();
    // copy form
    let newForm = recipeForm[0].cloneNode(true);
    newForm.hidden = false;

    // setting the text to search for in the HTML
    let formRegex = RegExp(`ingredients_needed-(\\d){1}-`, 'g');

    // generate form instance count
    formNum++;

    // add to fields values
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `ingredients_needed-${formNum}-`);
    container.appendChild(newForm);

    // update the total forms value setting expected fields to accept
    totalForms.setAttribute('value', `${formNum + 1}`);

    // Update variable list
    recipeForm = document.querySelectorAll(".multiField");

    // update view of remove ingredient btns
    renderRemBtns();
    // console.log("Run the function!", e);
}

function removeForm(e) {
    // get number of field and set hidden
    console.log(e);
    // recipeForm[e].hidden = true;
    recipeForm[e].getElementsByClassName('.checkboxinput')[0].checked = true;

    // set delete checkbox to true


}


// Function will run at onload and everytime an ingredient form is added
// we need this at the start in case the form is refreshed or prepopulated from GET
// the remove button is added per delete checkbox available in the form
function renderRemBtns() {
    let deleteChecks = container.querySelectorAll('.checkboxinput');

    // template for the new remove ingredient button
    const remBtn = document.createElement('button');
    const btnText = document.createTextNode("Remove ingredient");
    remBtn.appendChild(btnText);
    remBtn.setAttribute('onclick', `removeForm(x)`);
    remBtn.setAttribute('type', 'button');
    remBtn.classList.add('remove-form');

    // set the counter
    let counter = 0;

    // iterate through the delete checkboxes
    for (let checkbox of deleteChecks) {
        // find if given parent of checkbox contains any buttons like ours
        let el = checkbox.parentElement.querySelectorAll('.remove-form');
        // copy our template button to append
        let newRemBtn = remBtn.cloneNode(true);

        // if list el returned empty add our button
        if (el.length == 0) {
            checkbox.after(newRemBtn);
            // on adding button, refresh list so we can setAttr below
            el = checkbox.parentElement.querySelectorAll('.remove-form');
        }

        // setAttr with appropriate name
        el[0].setAttribute('onclick', `removeForm(${counter})`);

        counter++;
    }

}
