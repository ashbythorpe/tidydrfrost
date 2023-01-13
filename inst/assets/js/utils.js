function sort_by_rank(rank) {
  let list = $(".ui-sortable");
  let unsorted = list.find("div")
  let els = rank.map(i => unsorted[i]);
  $.each(els, function(idx, item) {
    list.append(item);
  });
};

window.localStorage.setItem("sort_by_rank", sort_by_rank);

function swap_sortable_elems() {
  let list = $(".ui-sortable");
  let el = list.find("div")[0];
  list.append(el);
};

window.localStorage.setItem("swap_sortable_elems", swap_sortable_elems);

function parse_mathjax(elem, exp = false) {
  let remove = [
    "\\\\begin", "\\\\end", /{[a-zA-Z]{2,}?}/g, "&", "\\\\quad", "\\t", "\\n"
  ]
  let item = MathJax.startup.document.getMathItemsWithin(elem)[0];
  let math = item.math
  final = remove.reduce((x, y) => x.replaceAll(y, ""), math)
  if (!exp) {
    // Replace 'e' variable with r_m
    final = final.replace(/(?<!\\[a-zA-Z]*)e/g, "r_m")
  }
  return final
}

window.localStorage.setItem("parse_mathjax", parse_mathjax);
