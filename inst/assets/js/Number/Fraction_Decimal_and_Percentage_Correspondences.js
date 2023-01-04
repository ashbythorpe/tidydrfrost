function get_filled_percentage() {
  let calc = $(".desmos").data("calculator");
  let exprs = calc.getExpressions();
  let last = exprs.slice(-1)[0].latex;
  let last_numbers = Array.from(last.matchAll(/[0-9]+/g)).map(x => Number(x[0]));
  let width = last_numbers[2];
  let height = last_numbers[3];
  let total = width * height;
  let fill = 0;
  let full_fill = exprs.find(x => x.id == "nl");
  if (full_fill != null) {
    let full_numbers = Array.from(full_fill.latex.matchAll(/[0-9]+/g)).map(x => Number(x[0]));
    fill += (height - full_numbers[7]) * width;
  }
  let extra_expr = exprs.find(x => x.id == "nc");
  if (extra_expr != null) {
    let latex = extra_expr.latex;
    let numbers = Array.from(latex.matchAll(/[0-9]+/g)).map(x => Number(x[0]));
    fill += numbers[2];
  };
  return Math.round(fill / total * 100);
}

window.localStorage.setItem("get_filled_percentage", get_filled_percentage)
