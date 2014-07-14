def estimate_pi_parallel(N, lview, N_per_trial=1E6):
    result = lview.map(estimate_pi, [N_per_trial for i in range(N)])
    while not result.ready():
        print(result.progress)
        time.sleep(0.5)
    return np.mean(list(result))

estimate_pi_parallel(100, lview)
