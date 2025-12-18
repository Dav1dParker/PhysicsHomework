import numpy as np
import matplotlib.pyplot as plt

from rotation_matrixes import A_x, A_z


def w(t):
    return np.array([0.0, 1.0, 0.0])  # rotation about world Y


def main():
    delta_t = 0.01
    steps = 10

    t_i = 0.0
    psi_i = 0.0
    tetta_i = 1e-4  # near the singularity (theta ≈ 0)
    phi_i = 0.0

    times, psi_deg, phi_deg, tetta_deg = [], [], [], []

    for _ in range(steps):
        A_i = A_z(np.degrees(psi_i)) @ A_x(np.degrees(tetta_i)) @ A_z(np.degrees(phi_i))
        p, q, r = A_i.T @ w(t_i)

        psi_i_dot = (1 / np.sin(tetta_i)) * (p * np.sin(phi_i) + q * np.cos(phi_i))
        tetta_i_dot = p * np.cos(phi_i) - q * np.sin(phi_i)
        phi_i_dot = r - (1 / np.tan(tetta_i)) * (p * np.sin(phi_i) + q * np.cos(phi_i))

        psi_i += psi_i_dot * delta_t
        tetta_i += tetta_i_dot * delta_t
        phi_i += phi_i_dot * delta_t
        t_i += delta_t

        times.append(t_i)
        psi_deg.append(np.degrees(psi_i))
        phi_deg.append(np.degrees(phi_i))
        tetta_deg.append(np.degrees(tetta_i))

    fig, axs = plt.subplots(2, 1, sharex=True, figsize=(8, 5))
    axs[0].plot(times, psi_deg, label='psi (deg)')
    axs[0].plot(times, phi_deg, label='phi (deg)')
    axs[0].legend()
    axs[0].set_ylabel('deg')
    axs[0].set_title('ψ и φ при θ → 0')

    axs[1].plot(times, tetta_deg, label='theta (deg)', color='tab:green')
    axs[1].set_xlabel('time (s)')
    axs[1].set_ylabel('deg')
    axs[1].legend()

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
