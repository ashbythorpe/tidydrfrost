function get_number_line_number() {
  let calc = $(".desmos").data("calculator");
  let exprs = calc.getExpressions();
  let labels = exprs.filter(x => x.id.includes('l'))
  let diff = Math.abs(Number(labels[0].label.replaceAll("`", "")) - Number(labels[1].label.replaceAll("`", "")))
  let label = labels.filter(x => /0,? /g.test(x.latex))[0].label
  let label_number = Number(label.replaceAll("`", ""))
  let expr = exprs.filter(x => /^c[0-9]$/g.test(x.id))[0];
  let offset = Number(/[0-9.\-]+/g.exec(expr.latex)[0])
  return label_number + offset * diff
}

window.localStorage.setItem("get_number_line_number", get_number_line_number)
