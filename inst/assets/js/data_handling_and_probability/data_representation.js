function bar_to_ignore() {
  let calc = $(".desmos-calculator").data("calculator");
  let exprs = calc.getExpressions().filter(x => x.id.includes("aY") || x.id.includes("fill"));
  let cond = exprs.map((x, i, a) => x.id.includes("fill") && i != 0 && a[i-1].id.includes("fill"));
  if (cond.some(x => x)) {
    let id = exprs[cond.indexOf(true)].id;
    let getnum = x => Number(/[0-9]+/g.exec(x)[0])
    return getnum(id)
  } else {
    return 0
  }
}

window.localStorage.setItem("bar_to_ignore", bar_to_ignore)

function get_bar_values() {
  let calc = $(".desmos").data("calculator");
  let latex = calc.getExpressions().filter(x => x.id.includes("a")).map(x => x.latex)
  return latex.map(x => Number(x.match(/[0-9]+(?=\))/g)[3]))
}

window.localStorage.setItem("get_bar_values", get_bar_values)

function set_expressions(values) {
  let calc = $('.desmos-calculator').data('calculator');
  values.map((x, i) => {
    calc.setExpression({
      id: 'aY' + String(i),
      latex: 'y_' + String(i + 1) + '=' + String(x)
    });
  });
}

window.localStorage.setItem("set_expressions", set_expressions)
