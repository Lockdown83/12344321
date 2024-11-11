function countTo56(num = 1) {  // Define a function that takes a number, starting at 1 by default
    if (num > 56) return;  // Base case: if the number exceeds 56, stop the recursion
    console.log(num);  // Print the current number to the console
    countTo56(num + 1);  // Recursive call: increment the number and call the function again
}

countTo56();  // Start the counting from 1
