document.addEventListener('DOMContentLoaded', () => {
  
  // set important variables
  var foods_dic = {};
  var prices_dic = {};
  var cats_selector = document.getElementById("cats_choice");
  var foods_selector = document.getElementById("foods_choice");
  var prices_selector = document.getElementById("prices_choice");
  var toppings_selector = document.getElementsByName('topping');

  // change selectors style to hidden
  document.getElementById('foods_selector').style.display = 'none';
  document.getElementById('prices_selector').style.display = 'none';
  document.getElementById('toppings_selector').style.display = 'none';

  // set event on selecting a category (adding to cart)
  cats_selector.onchange = () => {
    // get the selected category with index 
    var index = cats_selector.selectedIndex;
    var selected_cat = (cats_selector.options[index].value);
    // add a key of selected category in foods_dic
    foods_dic[`${selected_cat}`] = []
    // get all food items of selected category from the menu
    var foods_cat = document.getElementsByClassName(`${selected_cat}${index}`)
    for (i = 0; i < foods_cat.length; i++) {
      // add food items to the dict
      foods_dic[`${selected_cat}`].push(foods_cat[i].innerHTML);
    }
    // Empty the foods selector options
    while (foods_selector.options.length) {
      foods_selector.remove(0);
    }
    // adding empty choice in the selector
    let empty_choice = new Option('Choose Item ...', '')
    foods_selector.options.add(empty_choice)
    // put the food items in the selector as options
    var foods_list = foods_dic[`${selected_cat}`]
    if (foods_list) {
      for (i = 0; i < foods_list.length; i++) {
        let afood = new Option(foods_list[i], foods_list[i]);
        foods_selector.options.add(afood);
      }
    }
    document.getElementById('foods_selector').style.display = 'block';
  };

  // set event on selecting a food item (adding to cart)
  foods_selector.onchange = () => {
    // get the selected category with index 
    var index = cats_selector.selectedIndex;
    var selected_cat = (cats_selector.options[index].value);
    // get the selected food value
    let index1 = foods_selector.selectedIndex;
    var selected_food = (foods_selector.options[index1].value);
    // create new key for the selected food item's prices list
    prices_dic[`${selected_food}`] = []
    // get all prices for that food from the menu
    let foods_prices = document.getElementsByClassName(`${selected_cat}-${selected_food}`)
    for (let i = 0; i < foods_prices.length; i++) {
      prices_dic[`${selected_food}`].push(foods_prices[i].innerHTML);
    }
    // prepare the foods selection
    while (prices_selector.options.length) {
      prices_selector.remove(0);
    }
    // adding empty choice in the selector
    let empty_choice = new Option('Choose Item ...', '')
    prices_selector.options.add(empty_choice)
    
    var prices_list = prices_dic[`${selected_food}`]
    // put the food items in the selection element
    if (prices_list) {
      for (let i = 0; i < prices_list.length; i++) {
        var aprice = new Option(prices_list[i], i);
        prices_selector.options.add(aprice);
      }
    }
    document.getElementById('prices_selector').style.display = 'block';
  };

  // set event on selecting a size(price) item (adding to cart)
  prices_selector.onchange = () => {
    let selected_cat_i = document.getElementById("cats_choice").selectedIndex;
    let selected_cat = document.getElementById("cats_choice").options[selected_cat_i].value;
    if (selected_cat_i <= 2) {
      console.log(food_topping_limit());
      if (food_topping_limit() != 0) {
        document.getElementById('toppings_selector').style.display = 'block';
      }
    }else {
      document.getElementById('toppings_selector').style.display = 'none';
    }
  };

  // set event on selecting a topping item (adding to cart)
  for (let i=0; i<toppings_selector.length; i++){
    toppings_selector[i].onchange = () => {
      let limit = food_topping_limit()

      // find checked boxes and the rest
      let markedBoxCount = document.querySelectorAll('input[type="checkbox"]:checked').length;
      let unmarkedBoxCount = document.querySelectorAll('input[type="checkbox"]:not(:checked)');

      // apply the limit
      if (markedBoxCount >= limit) {
        for (let i = 0; i < unmarkedBoxCount.length; i++)
          unmarkedBoxCount[i].disabled = true;
      } else {
        for (let i = 0; i < unmarkedBoxCount.length; i++)
          unmarkedBoxCount[i].disabled = false;
      }
    };
  }
  document.querySelector("button[type='submit']").onclick = () => {
    
  }

  document.getElementById("place_order").onclick = () => {
    alert('are you shure you want to place this order ?');
    return true;
  }
});

// find the toppings no (limit) of selected food item
function food_topping_limit() {
  let selected_cat_i = document.getElementById("cats_choice").selectedIndex;
  let selected_cat = document.getElementById("cats_choice").options[selected_cat_i].value;
  let afood_list = document.getElementsByClassName(`${selected_cat}${selected_cat_i}`);
  let selected_food_id = document.getElementById("foods_choice").selectedIndex;
  let selected_food = document.getElementById("foods_choice").options[selected_food_id].value;
  for (let e=0; e < afood_list.length; e++) {
    if (afood_list[e].innerHTML === selected_food) {
      return afood_list[e].dataset.topping;
    }
  }
}