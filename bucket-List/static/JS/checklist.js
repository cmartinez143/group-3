//var label= document.createElement("label");
//var description = document.createTextNode(pair);
//var checkbox = document.createElement("input");

//checkbox.type = "checkbox";    // make the element a checkbox
//checkbox.name = "slct[]";      // give it a name we can check on the server side
//checkbox.value = pair;         // make its value "pair"

//label.appendChild(checkbox);   // add the box to the element
//label.appendChild(description);// add the description to the element

// add the label element to your div
//document.getElementById('list').appendChild(label);
   var i = 0;
    function addValue() {
       var v = document.form1.txtValue.value;
       // get the TextBox Value and assign it into the variable
       AddOpt = new Option(v, v);
       document.form1.lstValue.options[i++] = AddOpt;
       return true;
    }
    function deleteValue() {
       var s = 1;
       var Index;
       if (document.form1.lstValue.selectedIndex == -1) {
          alert("Please select any item from the ListBox");
          return true;
       }
       while (s > 0) {
           Index = document.form1.lstValue.selectedIndex;
           if (Index >= 0) {
                document.form1.lstValue.options[Index] = null;
                 --i;
           }
           else
              s = 0;
       }
       return true;
   }
       