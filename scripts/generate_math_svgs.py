import os
import matplotlib
import matplotlib.pyplot as plt

# Matplotlib configuration for crisp LaTeX math rendering
matplotlib.rcParams['mathtext.fontset'] = 'cm'  # Computer Modern (Standard LaTeX / Wikipedia style)
matplotlib.rcParams['mathtext.rm'] = 'serif'

FORMULAS_DIR = os.path.join('docs', 'research', 'formulas')
os.makedirs(FORMULAS_DIR, exist_ok=True)

formulas = [
    {
        'id': 'formula_01_sector_current',
        'lines': [
            r'i_k(t) = \frac{\mathrm{d}q_k}{\mathrm{d}t} = C_k(\theta) \cdot \frac{\mathrm{d}u_k}{\mathrm{d}t} + u_k(t) \cdot \frac{\mathrm{d}C_k(\theta)}{\mathrm{d}\theta} \cdot \omega'
        ],
        'figsize': (8.8, 1.2),
        'fontsize': 16,
    },
    {
        'id': 'formula_02_edge_field',
        'lines': [
            r'E_{\mathrm{edge}} \approx \frac{U}{r_{\mathrm{wire}} \cdot \ln(d / r_{\mathrm{wire}})} \gg E_{\mathrm{planar}}'
        ],
        'figsize': (6.8, 1.2),
        'fontsize': 16,
    },
    {
        'id': 'formula_03_zero_work_cycle',
        'lines': [
            r'W_{\mathrm{netto}} = \oint \tau_e(\theta)\,\mathrm{d}\theta = \oint \frac{1}{2}\,U^2(\theta)\,\frac{\mathrm{d}C}{\mathrm{d}\theta}\,\mathrm{d}\theta = 0 \quad (\mathrm{ohne\ Diode})'
        ],
        'figsize': (9.2, 1.2),
        'fontsize': 16,
    },
    {
        'id': 'formula_04_total_torque_sum',
        'lines': [
            r'\tau_e(\theta) = \frac{1}{2} \sum_{k=1}^{N} U_k^2(\theta) \cdot \frac{\mathrm{d}C_k(\theta)}{\mathrm{d}\theta}'
        ],
        'figsize': (6.5, 1.2),
        'fontsize': 16,
    },
    {
        'id': 'formula_05_mean_torque_integral',
        'lines': [
            r'\bar{\tau}_e = \frac{1}{2\pi} \int_{0}^{2\pi} \tau_e(\theta)\,\mathrm{d}\theta > 0 \quad (\bar{\tau}_e > \tau_{\mathrm{fric}} + \tau_{\mathrm{aero}})'
        ],
        'figsize': (8.2, 1.2),
        'fontsize': 16,
    },
    {
        'id': 'formula_06_power_balance',
        'lines': [
            r'P_{\mathrm{out}}(t) = P_{\mathrm{mech, in}}(t) + P_{\mathrm{elec, in}}(t) - \frac{\mathrm{d}W_{\mathrm{stored}}}{\mathrm{d}t} - P_{\mathrm{loss}}'
        ],
        'figsize': (8.5, 1.2),
        'fontsize': 16,
    },
    {
        'id': 'formula_07_generator_output',
        'lines': [
            r'I_{\mathrm{gen}} = N \cdot \Delta C \cdot U \cdot n = 50 \cdot (50 \cdot 10^{-12}\,\mathrm{F}) \cdot (20 \cdot 10^3\,\mathrm{V}) \cdot 1\,\mathrm{s}^{-1} = 50\,\mu\mathrm{A}',
            r'P_{\mathrm{elec}} = U \cdot I_{\mathrm{gen}} = 20\,\mathrm{kV} \cdot 50\,\mu\mathrm{A} = 1{,}0\,\mathrm{Watt}',
            r'I_{\mathrm{out, max}} = \frac{P_{\mathrm{elec}}}{U_{\mathrm{out}}} = \frac{1{,}0\,\mathrm{W}}{300\,\mathrm{V}} \approx 3{,}3\,\mathrm{mA}'
        ],
        'figsize': (11.0, 2.6),
        'fontsize': 15,
    },
    {
        'id': 'formula_08_pulse_storage_10s',
        'lines': [
            r'W_{\mathrm{Lampe}} = P \cdot t = 1000\,\mathrm{W} \cdot 10\,\mathrm{s} = 10\,\mathrm{kJ} = 2{,}78\,\mathrm{Wh}',
            r'C_{\mathrm{erf}} = \frac{2 \cdot W}{U^2} = \frac{2 \cdot 10\,000\,\mathrm{J}}{(15\,000\,\mathrm{V})^2} \approx 88{,}9\,\mu\mathrm{F} \quad (\mathrm{bei\ 15\ kV})'
        ],
        'figsize': (9.5, 1.9),
        'fontsize': 15,
    },
    {
        'id': 'formula_09_continuous_storage_1h',
        'lines': [
            r'W_{\mathrm{1h}} = P \cdot t = 1000\,\mathrm{W} \cdot 3600\,\mathrm{s} = 3{,}6\,\mathrm{MJ} = 1\,\mathrm{kWh}',
            r'C_{\mathrm{erf}} = \frac{2 \cdot W}{U^2} = \frac{2 \cdot 3\,600\,000\,\mathrm{J}}{(20\,000\,\mathrm{V})^2} = 18\,000\,\mu\mathrm{F} = 18\,\mathrm{mF} \quad (\mathrm{bei\ 20\ kV})'
        ],
        'figsize': (9.5, 1.9),
        'fontsize': 15,
    },
    {
        'id': 'formula_10_energy_conservation_integral',
        'lines': [
            r'\Delta E = \int_{0}^{T} P_{\mathrm{out}}(t)\,\mathrm{d}t - \int_{0}^{T} P_{\mathrm{in}}(t)\,\mathrm{d}t - \Delta W_{\mathrm{stored}} \leq 0'
        ],
        'figsize': (8.5, 1.2),
        'fontsize': 16,
    }
]

for item in formulas:
    n_lines = len(item['lines'])
    fig = plt.figure(figsize=item['figsize'], dpi=300)
    fig.patch.set_alpha(0.0)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.patch.set_alpha(0.0)
    
    if n_lines == 1:
        ax.text(0.5, 0.5, f"${item['lines'][0]}$", fontsize=item['fontsize'], color='#e6edf3', ha='center', va='center')
    else:
        y_positions = [1.0 - (i + 0.5) / n_lines for i in range(n_lines)]
        for y, line in zip(y_positions, item['lines']):
            ax.text(0.5, y, f"${line}$", fontsize=item['fontsize'], color='#e6edf3', ha='center', va='center')
    
    out_svg = os.path.join(FORMULAS_DIR, f"{item['id']}.svg")
    plt.savefig(out_svg, format='svg', transparent=True, bbox_inches='tight', pad_inches=0.08)
    plt.close(fig)
    
    # Post-process SVG to add responsive light/dark CSS styling
    with open(out_svg, 'r', encoding='utf-8') as f:
        content = f.read()
    
    css_injection = """
<style>
  path { fill: #e6edf3 !important; }
  @media (prefers-color-scheme: light) {
    path { fill: #1f2328 !important; }
  }
</style>
"""
    content = content.replace('</svg>', f'{css_injection}</svg>')
    with open(out_svg, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Generated: {out_svg}")

print("All math SVGs successfully created!")
