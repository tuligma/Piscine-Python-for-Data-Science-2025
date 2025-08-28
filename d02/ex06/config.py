file = "data.csv"
num_of_steps = 3
filename = "report"
reportfile = filename + '.txt'
template = (
    "Report\nWe have made {lines} "
    "observations from tossing a coin: {t_count}"
    " of them were tails and {h_count} of\nthem were heads. "
    "The probabilities are {t_fraction:.2f}% "
    "and {h_fraction:.2f}%, respectively. Our\n"
    "forecast is that in the next {predict} observations we will have: "
    "{p_t_count} tail and {p_h_count} heads.\n"
)
