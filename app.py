import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CatalystAI",
    page_icon="⚗️",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("⚗️ CatalystAI")

page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "Discovery",
        "Candidates",
        "3D Reaction Studio",
        "Ranking",
        "Feedback Loop",
        "Export"
    ]
)

# Pages

if page == "Home":
    st.title("⚗️ CatalystAI")
    st.subheader("AI Platform for Molecular Discovery in Sustainable Fuels")
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(circle at 20% 20%, rgba(56,189,248,0.15), transparent 25%),
            radial-gradient(circle at 80% 30%, rgba(167,139,250,0.14), transparent 25%),
            radial-gradient(circle at 50% 80%, rgba(34,197,94,0.10), transparent 25%),
            linear-gradient(135deg, #020617, #0f172a, #111827);
    }

    .particle {
        position: fixed;
        width: 8px;
        height: 8px;
        background: #38bdf8;
        border-radius: 50%;
        box-shadow: 0 0 18px #38bdf8;
        animation: floatParticles 9s infinite ease-in-out;
        z-index: 0;
    }

    .p1 { top: 18%; left: 12%; animation-delay: 0s; }
    .p2 { top: 35%; left: 85%; animation-delay: 1s; background:#a78bfa; box-shadow:0 0 18px #a78bfa; }
    .p3 { top: 70%; left: 20%; animation-delay: 2s; background:#22c55e; box-shadow:0 0 18px #22c55e; }
    .p4 { top: 78%; left: 75%; animation-delay: 3s; }
    .p5 { top: 48%; left: 50%; animation-delay: 4s; background:#a78bfa; box-shadow:0 0 18px #a78bfa; }

    @keyframes floatParticles {
        0% { transform: translateY(0px) scale(1); opacity: 0.4; }
        50% { transform: translateY(-35px) scale(1.5); opacity: 1; }
        100% { transform: translateY(0px) scale(1); opacity: 0.4; }
    }
    </style>

    <div class="particle p1"></div>
    <div class="particle p2"></div>
    <div class="particle p3"></div>
    <div class="particle p4"></div>
    <div class="particle p5"></div>
    """, unsafe_allow_html=True)
    atom_animation = """
    <div style="
        background: linear-gradient(135deg, #020617, #0f172a, #111827);
        border-radius: 24px;
        padding: 30px;
        margin-top: 20px;
        margin-bottom: 25px;
        box-shadow: 0 0 35px rgba(56, 189, 248, 0.25);
        text-align: center;
        color: white;
        overflow: hidden;
    ">

    <style>
    .atom-container {
        position: relative;
        width: 260px;
        height: 260px;
        margin: auto;
    }

    .nucleus {
        position: absolute;
        width: 55px;
        height: 55px;
        background: radial-gradient(circle, #38bdf8, #2563eb);
        border-radius: 50%;
        top: 102px;
        left: 102px;
        box-shadow: 0 0 30px #38bdf8;
    }

    .orbit {
        position: absolute;
        width: 230px;
        height: 90px;
        border: 2px solid rgba(125, 211, 252, 0.55);
        border-radius: 50%;
        top: 85px;
        left: 15px;
        animation: spin 4s linear infinite;
    }

    .orbit.two {
        transform: rotate(60deg);
        animation-duration: 5s;
    }

    .orbit.three {
        transform: rotate(120deg);
        animation-duration: 6s;
    }

    .electron {
        width: 16px;
        height: 16px;
        background: #a78bfa;
        border-radius: 50%;
        box-shadow: 0 0 18px #a78bfa;
        position: absolute;
        top: 36px;
        left: 105px;
    }

    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    .glow-text {
        font-size: 28px;
        font-weight: 800;
        margin-top: 12px;
        background: linear-gradient(90deg, #38bdf8, #a78bfa, #22c55e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    </style>

    <div class="atom-container">    
        <div class="nucleus"></div>
        <div class="orbit"><div class="electron"></div></div>
        <div class="orbit two"><div class="electron"></div></div>
        <div class="orbit three"><div class="electron"></div></div>
    </div>

    <div class="glow-text">Accelerating Molecular Discovery with AI</div>
    <p style="color:#cbd5e1; font-size:16px;">
    From reaction input to AI-generated candidates, ranking, visualization, and experimental feedback.
    </p>

    </div>
    """

    components.html(atom_animation, height=420)

    st.markdown("## Platform Highlights")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="
            background:#0f172a;
            padding:22px;
            border-radius:20px;
            border:1px solid #38bdf8;
            box-shadow:0 0 20px rgba(56,189,248,0.18);
            height:210px;
        ">
        <h3 style="color:#38bdf8;">🧪 AI Candidate Generation</h3>
        <p style="color:#cbd5e1;">
        Suggests known and novel catalyst/enzyme candidates for sustainable fuel reactions.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="
                background:#0f172a;
            padding:22px;
            border-radius:20px;
            border:1px solid #a78bfa;
            box-shadow:0 0 20px rgba(167,139,250,0.18);
            height:210px;
        ">
        <h3 style="color:#a78bfa;">🧬 3D Reaction Studio</h3>
        <p style="color:#cbd5e1;">
        Visualizes molecular structures and catalyst interaction using an interactive 3D viewer.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="
            background:#0f172a;
            padding:22px;
            border-radius:20px;
            border:1px solid #22c55e;
            box-shadow:0 0 20px rgba(34,197,94,0.18);
            height:210px;
        ">
        <h3 style="color:#22c55e;">🔁 Feedback Learning Loop</h3>
        <p style="color:#cbd5e1;">
        Compares predicted vs actual lab outcomes and improves future discovery decisions.
        </p>
    </div>
        """, unsafe_allow_html=True)

    if "reaction" in st.session_state:
        st.info(f"Current target reaction: {st.session_state['reaction']}")
    else:
        st.warning("No reaction selected yet. Go to Discovery page first.")

    st.markdown("""
    ### What CatalystAI Does

    CatalystAI helps researchers discover and optimize catalysts, enzymes,
    and microbial pathways for sustainable fuel and chemical production.

    ### End-to-End Workflow

    1. Enter target reaction  
    2. Retrieve known catalysts or enzymes  
    3. Generate novel AI candidates  
    4. Rank by activity, selectivity, and stability  
    5. Visualize molecules in 3D  
    6. Log experimental results  
    7. Improve future predictions using feedback  

    ### Prototype Modules

    - Discovery Input
    - Candidate Generation
    - Ranking Dashboard
    - 3D Reaction Studio
    - Feedback Loop
    - Export Report
    """)




elif page == "Discovery":
    st.title("🔬 Discovery Page")
    st.subheader("Enter your target reaction")

    reaction = st.text_input(
        "Target Reaction",
        placeholder="Example: CO2 + Green H2 → Methanol"
    )

    domain = st.selectbox(
        "Choose Discovery Direction",
        [
            "Chemical Catalysis",
            "Synthetic Biology",
            "Both"
        ]
    )

    goal = st.multiselect(
        "Optimization Goal",
        [
            "High Activity",
            "High Selectivity",
            "High Stability",
            "Low Cost",
            "Low Energy Requirement"
        ]
    )

    st.subheader("Reaction Conditions")

    col1, col2, col3 = st.columns(3)

    with col1:
        temperature = st.number_input("Temperature (°C)", value=250)

    with col2:
        pressure = st.number_input("Pressure (bar)", value=30)

    with col3:
        time = st.number_input("Reaction Time (hours)", value=5)

    if st.button("Generate Discovery Plan"):
        if reaction == "":
            st.warning("Please enter a target reaction first.")
        else:
            st.success("Discovery plan generated successfully!")

            st.session_state["reaction"] = reaction
            st.session_state["domain"] = domain
            st.session_state["goal"] = goal
            st.session_state["temperature"] = temperature
            st.session_state["pressure"] = pressure
            st.session_state["time"] = time

            st.write("### Your Discovery Setup")
            st.write(f"**Reaction:** {reaction}")
            st.write(f"**Direction:** {domain}")
            st.write(f"**Goals:** {', '.join(goal) if goal else 'Not selected'}")
            st.write(f"**Temperature:** {temperature} °C")
            st.write(f"**Pressure:** {pressure} bar")
            st.write(f"**Reaction Time:** {time} hours")


elif page == "Candidates":
    st.title("🧪 Candidate Generation")

    if "reaction" not in st.session_state:
        st.warning("Please go to Discovery page first and generate a reaction.")
    else:
        st.success(f"Generating candidates for: {st.session_state['reaction']}")

        import pandas as pd
        import random

        # Known catalysts (mock data)
        known = pd.DataFrame({
            "Catalyst": ["Cu", "Zn", "Cu-Zn", "Ni"],
            "Activity": [75, 70, 85, 65],
            "Stability": [80, 78, 82, 75]
        })

        st.subheader("Known Catalysts")
        st.dataframe(known)

        # AI Generated catalysts (fake but smart-looking)
        generated_names = [
            "Cu-Zn-Al Nano Catalyst",
            "Ni-Cu Hybrid Structure",
            "Fe-based Advanced Catalyst"
        ]

        generated = pd.DataFrame({
            "Catalyst": generated_names,
            "Activity": [random.randint(70, 95) for _ in range(3)],
            "Stability": [random.randint(70, 90) for _ in range(3)]
        })

        st.subheader("AI Generated Catalysts")
        st.dataframe(generated)

        # Combine & rank
        combined = pd.concat([known, generated])
        combined["Score"] = combined["Activity"] * 0.6 + combined["Stability"] * 0.4
        combined = combined.sort_values(by="Score", ascending=False)

        st.subheader("Ranked Candidates")
        st.dataframe(combined)
        st.subheader("📊 Performance Visualization")

        fig = px.scatter(
            combined,
            x="Activity",
            y="Stability",
            size="Score",
            text="Catalyst",
            title="Activity vs Stability"
        )

        fig.update_traces(textposition="top center")

        st.plotly_chart(fig, use_container_width=True)
        st.subheader("🏆 Top 3 Recommended Candidates")

        top3 = combined.head(3)

        cols = st.columns(3)

        for index, row in enumerate(top3.itertuples()):
            with cols[index]:
                st.metric(
                    label=row.Catalyst,
                    value=f"{row.Score:.1f}",
                    delta="Recommended"
                )
                st.write(f"Activity: {row.Activity}")
                st.write(f"Stability: {row.Stability}")        


elif page == "3D Reaction Studio":
    st.title("🧬 3D Reaction Studio")

    if "reaction" not in st.session_state:
        st.warning("Please go to Discovery page first.")
    else:
        st.success(f"Visualizing reaction: {st.session_state['reaction']}")
        col1, col2, col3 = st.columns(3)

        with col1:
            molecule = st.selectbox(
                "Select Molecule View",
                ["Methanol Demo", "CO2 Demo", "Hydrogen Demo"]
            )

        with col2:
            catalyst = st.selectbox(
                "Select Catalyst Surface",
                ["Cu-Zn-Al", "Ni-Cu Hybrid", "Fe-based Catalyst"]
            )        

        with col3:
            mode = st.selectbox(
                "View Mode",
                ["Molecule Structure", "Catalyst Interaction", "Reaction Pathway"]
            )

        st.subheader("3D Molecular View")
        html_code = """
        <!DOCTYPE html>
        <html>
        <head>
        <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
        </head>

        <body style="margin:0; background:black;">
        <div id="viewer" style="width:100%; height:400px; position:relative;"></div>

        <script>
        var element = document.getElementById("viewer");
        var viewer = $3Dmol.createViewer(element, { backgroundColor: "black" });

        var xyzData = `5
        Methane
        C 0.000 0.000 0.000
        H 0.629 0.629 0.629
        H -0.629 -0.629 0.629
        H 0.629 -0.629 -0.629
        H -0.629 0.629 -0.629
        `;

        viewer.addModel(xyzData, "xyz");
        viewer.setStyle({}, {stick:{radius:0.18}, sphere:{scale:0.35}});
        viewer.zoomTo();
        viewer.render();
        viewer.zoom(1.2);
        </script>
        </body>
        </html>
        """        

        components.html(html_code, height=400)
        st.subheader("🧠 Reaction Insights")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Predicted Activity", "87%")

        with col2:
            st.metric("Selectivity", "82%")

        with col3:
            st.metric("Stability", "79%")

        with col4:
            st.metric("Energy Barrier", "Low")

        st.info(
            f"The selected {catalyst} catalyst may improve reaction performance by lowering the energy barrier and improving molecular interaction."
        )               


elif page == "Ranking":
    st.title("📊 Ranking & Comparison")

    if "reaction" not in st.session_state:
        st.warning("Please go to Discovery page first and generate a reaction.")
    else:
        st.success(f"Ranking candidates for: {st.session_state['reaction']}")

        import pandas as pd
        import random

        known = pd.DataFrame({
            "Candidate": ["Cu", "Zn", "Cu-Zn", "Ni"],
            "Type": ["Known Catalyst", "Known Catalyst", "Known Catalyst", "Known Catalyst"],
            "Activity": [75, 70, 85, 65],
            "Selectivity": [78, 72, 88, 70],
            "Stability": [80, 78, 82, 75],
            "Cost Score": [85, 90, 80, 88]
        })

        generated = pd.DataFrame({
            "Candidate": [
                "Cu-Zn-Al Nano Catalyst",
                "Ni-Cu Hybrid Structure",
                "Fe-based Advanced Catalyst"
            ],
            "Type": ["AI Generated", "AI Generated", "AI Generated"],
            "Activity": [random.randint(78, 95) for _ in range(3)],
            "Selectivity": [random.randint(75, 92) for _ in range(3)],
            "Stability": [random.randint(72, 90) for _ in range(3)],
            "Cost Score": [random.randint(70, 90) for _ in range(3)]
        })

        ranking_df = pd.concat([known, generated], ignore_index=True)

        ranking_df["Final Score"] = (
            ranking_df["Activity"] * 0.35 +
            ranking_df["Selectivity"] * 0.30 +
            ranking_df["Stability"] * 0.25 +
            ranking_df["Cost Score"] * 0.10
        )

        ranking_df = ranking_df.sort_values(by="Final Score", ascending=False)

        st.subheader("🏆 Final Ranked Candidates")
        st.dataframe(ranking_df, use_container_width=True)

        st.subheader("📈 Candidate Score Comparison")

        fig = px.bar(
            ranking_df,
            x="Candidate",
            y="Final Score",
            color="Type",
            title="Final Candidate Ranking Score"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.subheader("🎯 Best Candidate Recommendation")

        best = ranking_df.iloc[0]

        st.success(
            f"Recommended Candidate: {best['Candidate']} "
            f"with score {best['Final Score']:.2f}"
        )

        st.write(
            "This candidate is recommended based on a weighted combination of "
            "activity, selectivity, stability, and cost score."
        )


elif page == "Feedback Loop":
    st.title("🔁 Feedback Loop")

    if "reaction" not in st.session_state:
        st.warning("Please go to Discovery page first.")
    else:
        st.success(f"Logging results for: {st.session_state['reaction']}")

        st.subheader("🧪 Enter Experimental Results")

        catalyst = st.text_input("Catalyst Tested", placeholder="e.g., Cu-Zn-Al Nano Catalyst")

        actual_yield = st.slider("Actual Yield (%)", 0, 100, 50)
        selectivity = st.slider("Selectivity (%)", 0, 100, 50)
        stability = st.slider("Stability (%)", 0, 100, 50)

        notes = st.text_area("Lab Notes", placeholder="Observations from experiment")

        if st.button("Submit Experiment"):
           st.success("Experiment logged successfully!")

           st.write("### Submitted Data")
           st.write(f"Catalyst: {catalyst}")
           st.write(f"Yield: {actual_yield}%")
           st.write(f"Selectivity: {selectivity}%")
           st.write(f"Stability: {stability}%")
           st.write(f"Notes: {notes}")

    # --- Simulated Prediction ---
           predicted_yield = 80
           predicted_selectivity = 78

           st.subheader("📊 Prediction vs Actual")
       
           col1, col2 = st.columns(2)

           with col1:
               st.metric("Predicted Yield", f"{predicted_yield}%")
               st.metric("Predicted Selectivity", f"{predicted_selectivity}%")

           with col2:
               st.metric("Actual Yield", f"{actual_yield}%")
               st.metric("Actual Selectivity", f"{selectivity}%")

    # --- AI Insight ---
           st.subheader("🧠 AI Analysis")

           if actual_yield < predicted_yield:
               st.error("⚠️ Underperformance detected")
               st.write(
                   "Possible reason: Catalyst instability or poor reaction conditions. "
                   "Consider improving thermal stability or adding Zn-based modifiers."
               )
           elif actual_yield > predicted_yield:
               st.success("✅ Outperformed prediction!")
               st.write(
                   "Interesting result: Catalyst performed better than expected. "
                   "This suggests a beneficial structural property worth further study."
               )
           else:
               st.info("Performance matches prediction. Model is accurate.")

           st.subheader("🔁 Model Update")

           st.write(
               "The system will incorporate this experimental data to refine future predictions."
           )       
        st.write(f"Catalyst: {catalyst}")
        st.write(f"Yield: {actual_yield}%")
        st.write(f"Selectivity: {selectivity}%")
        st.write(f"Stability: {stability}%")
        st.write(f"Notes: {notes}")


elif page == "Export":
    st.title("📄 Export Report")

    if "reaction" not in st.session_state:
        st.warning("Please go to Discovery page first.")
    else:
        st.success("Your discovery report is ready.")

        report = f"""
CatalystAI Discovery Report

Target Reaction:
{st.session_state.get("reaction", "Not selected")}

Discovery Direction:
{st.session_state.get("domain", "Not selected")}

Optimization Goals:
{", ".join(st.session_state.get("goal", []))}

Reaction Conditions:
Temperature: {st.session_state.get("temperature", "N/A")} °C
Pressure: {st.session_state.get("pressure", "N/A")} bar
Reaction Time: {st.session_state.get("time", "N/A")} hours

Platform Workflow:
1. User enters target reaction
2. System retrieves known catalyst/enzyme candidates
3. AI generates novel candidate designs
4. Predictive model ranks candidates
5. 3D molecular reaction view visualizes interactions
6. Researcher logs experimental outcomes
7. Feedback loop improves future predictions

Key Prototype Features:
- Reaction discovery input
- Candidate generation
- Ranking system
- Performance visualization
- 3D molecular viewer
- Prediction vs actual feedback loop
- Exportable discovery report

Conclusion:
CatalystAI acts as an AI-powered research assistant for accelerating catalyst and synthetic biology discovery for sustainable fuel production.
"""

        st.text_area("Report Preview", report, height=400)

        st.download_button(
            label="Download Report",
            data=report,
            file_name="CatalystAI_Discovery_Report.txt",
            mime="text/plain"
        )