function find_place_value_index(number) {
  let calc = $(".desmos").data("calculator");
  let exprs = calc.getExpressions().filter(x => /^c[0-9]$/g.test(x.id));
  return exprs.map(x => x.latex.includes(String(number))).indexOf(true);
}

window.localStorage.setItem("find_place_value_index", find_place_value_index)

function get_place_value_number() {
  let calc = $(".desmos").data("calculator");
  let expr = calc.getExpressions().filter(x => /^c[0-9]$/g.test(x.id))[0];
  return Number(/[0-9.]+/g.exec(expr.latex)[0]);
}

window.localStorage.setItem("get_place_value_number", get_place_value_number)
