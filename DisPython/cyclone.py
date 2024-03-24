import streamlit as st

show_cyclone_page = False
# Title and Short Description
st.title("Cyclones: Be Prepared, Stay Safe")
st.write("This page provides information about cyclones and essential safety measures to take before, during, and after a cyclone event.")

# Image of Cyclone (replace with image URL)
st.image("https://placeholdit.img/600x400/cyan/fff/?text=Cyclone", width=600)

# Information about Cyclones
st.header("What are Cyclones?")
cyclone_info = """
Cyclones are intense rotating storm systems formed over warm tropical waters. They are characterized by strong winds, heavy rain, and storm surges that can cause significant damage and loss of life. 
"""
st.markdown(cyclone_info)

# Safety Measures - Heading
st.header("Cyclone Safety Measures")
st.subheader("Before a Cyclone:")
precautions_before = [
    "Stay informed: Monitor weather reports and warnings issued by official authorities.",
    "Prepare an emergency kit: Include non-perishable food, water, first-aid supplies, medications, flashlight, radio, etc.",
    "Secure your home: Trim trees, board up windows, and bring in outdoor furniture.",
    "Develop an evacuation plan: Identify a safe evacuation route and shelter location.",
    "Fill bathtubs and containers with clean water in case of disruptions."
]
st.markdown("\n".join(f"- {point}" for point in precautions_before))

# Safety Measures - During a Cyclone
st.subheader("During a Cyclone:")
precautions_during = [
    "Evacuate if instructed to do so by authorities.",
    "Stay indoors in a safe room away from windows and doors.",
    "Turn off utilities if flooding is a danger.",
    "Listen to the radio or local broadcasts for updates.",
    "Do not go outside until authorities declare it safe."
]
st.markdown("\n".join(f"- {point}" for point in precautions_during))

# Safety Measures - After a Cyclone
st.subheader("After a Cyclone:")
precautions_after = [
    "Stay away from downed power lines and damaged buildings.",
    "Be cautious of floodwaters and potential contamination.",
    "Report any injuries or damages to emergency services.",
    "Help others in need if it is safe to do so.",
    "Follow instructions from authorities regarding recovery efforts."
]
st.markdown("\n".join(f"- {point}" for point in precautions_after))

# Dos and Don'ts
st.header("Dos and Don'ts During a Cyclone")
dos_donts = {
    "Dos": [
        "Stay informed and listen to official warnings.",
        "Evacuate if instructed to do so.",
        "Secure your belongings and prepare an emergency kit.",
        "Stay indoors in a safe room during the storm.",
        "Help others in need if it is safe to do so."
    ],
    "Don'ts": [
        "Ignore official warnings or evacuation orders.",
        "Go outside during the storm surge or high winds.",
        "Drive through flooded areas.",
        "Use candles or open flames during power outages.",
        "Spread rumors or panic."
    ]
}

st.subheader("Dos:")
st.markdown("\n".join(f"- {point}" for point in dos_donts["Dos"]))

st.subheader("Don'ts:")
st.markdown("\n".join(f"- {point}" for point in dos_donts["Don'ts"]))

# Conclusion
st.subheader("Stay Prepared, Stay Safe!")
conclusion = """
By being informed and taking necessary precautions, you can significantly reduce the risks associated with cyclones. Remember, preparedness is key to staying safe during these natural disasters."""
st.markdown(conclusion)
