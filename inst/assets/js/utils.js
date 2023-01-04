function sort_by_rank(rank) {
  let list = $(".ui-sortable");
  let unsorted = list.find("div")
  let els = rank.map(i => unsorted[i]);
  $.each(els, function(idx, item) {
    list.append(item);
  });
}

window.localStorage.setItem("sort_by_rank", sort_by_rank)

function swap_sortable_elems() {
  let list = $(".ui-sortable");
  let el = list.find("div")[0];
  list.append(el);
}

window.localStorage.setItem("swap_sortable_elems", swap_sortable_elems)
