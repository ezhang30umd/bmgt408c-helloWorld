// Change text function
function changeText() {
    document.getElementById('changeText').innerText = 'Text changed!';
}

// Name form
document.getElementById('nameForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const name = document.getElementById('nameInput').value;
    document.getElementById('greeting').innerText = 'Hello, ' + name + '!';
});

// Favorite foods list
const foods = ['Hand-pulled noodles', 'Sushi', 'Texas BBQ'];
const foodList = document.getElementById('foodList');
for (let i = 0; i < foods.length; i++) {
    const li = document.createElement('li');
    li.innerText = foods[i];
    foodList.appendChild(li);
}

// Course checkboxes
const courses = ['BMGT408C', 'BMGT490H', 'CMSC429', 'CMSC335'];
const checkboxDiv = document.getElementById('checkboxes');
for (let i = 0; i < courses.length; i++) {
    const label = document.createElement('label');
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.value = courses[i];
    label.appendChild(checkbox);
    label.appendChild(document.createTextNode(' ' + courses[i]));
    checkboxDiv.appendChild(label);
    checkboxDiv.appendChild(document.createElement('br'));
}

// Display selected courses
function displayCourses() {
    const checkboxes = document.querySelectorAll('#checkboxes input:checked');
    const selected = [];
    for (let i = 0; i < checkboxes.length; i++) {
        selected.push(checkboxes[i].value);
    }
    document.getElementById('courseDisplay').innerText = 'Courses: ' + selected.join(', ');
}
