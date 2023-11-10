import streamlit as st
import json 

f = open("data.json", encoding="utf8")
options = json.load(f)

def main():
    st.title("🚀 ChatGPT Prompt Maker App")
    st.write(
        "Welcome to the ChatGPT Prompt Maker App! 🚀\n"
        "Follow these three easy steps to create a powerful prompt for ChatGPT:"
    )

    # Step 1
    st.header("Step 1: Answer Questions")
    st.write(
        "Answer the following questions as specifically as possible:"
    )

    # Questions
    user_name = st.text_input("1. 🤔 What's your name?")
    business_description = st.text_input("2. 🏢 Describe your business:")
    target_description = st.text_input("3. 🎯 Who is your target audience?")
    product_description = st.text_input("4. 🛍️ Describe your product:")
    special_words = st.text_input("5. 🗣️ Is there any specific words your target audience used? If yes, please list them:")
    if special_words == None:
        special_words = "-"
    # tonality = st.text_input("5. Choose the tonality (e.g., Persuasive, Informative, Friendly):")
    tonality = st.selectbox("🎙️ Landing Page Tonality", options["Tones"])
    tonality = tonality.split(" ")[1]

    # Step 2
    st.header("Step 2: Click 'Make Prompt' Button")
    st.write("Once you've answered all the questions, click the 'Make Prompt' button below:")

    if st.button("Make Prompt"):
        # Step 3
        st.header("Step 3: Copy the Prompt to ChatGPT")
        prompt = generate_prompt(user_name, business_description, target_description, product_description, tonality)
        st.code(prompt, language="text")
        st.success("Prompt generated! Copy the code above and use it with ChatGPT.")
        st.success("If ChatGPT only make one variation (the prompt will ask ChatGPT to make 3), just type 'continue your answer'")

def generate_prompt(user_name, business_description, target_description, product_description, tonality):
    prompt = f"""
    "Write three variations of a landing page for {business_description} targeted towards {target_description}.

    Product Description:
    {product_description}

    Please adhere to the following guidelines when creating each landing page:
    1. Notice Bar: Incorporate at least one of these elements: urgency or scarcity, guarantee, and trust seals.
    2. Subheadline: Expand on the headline by adding benefits or addressing how the product solves the target audience's pain points.
    3. VSL (Video Sales Letter): Provide a script following this outline:
       - Step 1: Make a bold claim
       - Step 2: Include a snippet of social proof
       - Step 3: Highlight the target audience's pain points and struggles
       - Step 4: Future pace the bold claim
       - Step 5: Include more social proof
       - Step 6: Establish company credibility
       - Step 7: Introduce the company
       - Step 8: Present the main benefits
       - Step 9: Describe high-level features
       - Step 10: Discuss the consequences of not taking action
       - Step 11: Remind the audience of the bold claim
       - Step 12: Include additional social proof
       - Step 13: Provide a compelling Call to Action (CTA).
    4. CTA Title: Create a CTA title that encourages the audience to take action.
    5. CTA Button: Ensure the CTA button's text aligns with the CTA title, and it should not exceed five words.
    6. Objections: List the objections that you'll address with real testimonials.
    7. Benefits: Enumerate the benefits clients/consumers will gain from using the product, ensuring they relate to other landing page components. Give a short description for each benefit. 
    8. 3 Steps Process: Explain the three-step process of how the company works, making it easy to understand for a high school graduate.
    9. About Us: Keep the 'About Us' section concise.
    10. FAQ: Answer the most common questions related to the product.
    11. Ensure that each component of the landing page is logically related to the others.
    
    Use these words anytime you can: {special_words}

    Compose each landing page in the specified {tonality} tone and use the following format:

    **Notice Bar**: <notice bar>
    **Headline**: <headline>
    **Subheadline**: <subheadline>
    **VSL**:
    <VSL>
    **CTA Title**: <CTA title>
    **CTA Button**: <CTA button>

    **Objections**:
    1. <Objection 1>
    2. <Objection 2>
    3. <Objection 3>

    **3 Steps Transformations**:
    1. <Transformation 1>
    2. <Transformation 2>
    3. <Transformation 3>

    **Benefits**:
    1. <Benefit 1>
    2. <Benefit 2>
    3. <Benefit 3>

    **3 Steps Process**:
    1. <Step 1>
    2. <Step 2>
    3. <Step 3>

    **About Us**:
    <about us>

    **FAQ**:
    <FAQ>
    """
    return prompt

if __name__ == "__main__":
    main()
