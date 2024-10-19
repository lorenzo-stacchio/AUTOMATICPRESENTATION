import os 
from tts_google import generate_audio
from pydub import AudioSegment
from moviepy.editor import *

dict_Diapositivatext = {
  "Diapositiva1": {
    "content": "Good morning, everyone. Today, I'm excited to share our work: 'XRAI-Ethics: Towards a Robust Ethical Analysis Framework for Extended Artificial Intelligence.' This work is a collaborative effort from a dedicated team, including myself, Lorenzo Stacchio, and my esteemed colleagues from both the University of Macerata and the Polytechnic University of Marche, all members of the Vision Robotics and Artificial Intelligence laboratory."
  },
  "Diapositiva2": {
    "content": "To beging, we know that XR have been rapidly gaining traction in various industries, particularly in entertainment, education, and healthcare. XR is foundational to the concept of the Metaverse, providing immersive experiences that allow users to interact with both real and virtual worlds in a seamless manner. This has opened up a realm of possibilities where people can work, learn, socialize, and even receive medical treatment in entirely new ways."
  },
  "Diapositiva3": {
    "content": "Our research is focused on exploring how we can create a robust ethical framework for XRAI, or Extended Artificial Intelligence, and today, I will walk you through why this work is so important for the future of technology, society, and human well-being. Let’s start by defining what we mean by XRAI and why it represents a significant step forward for the Metaverse and XR technologies."
  },
  "Diapositiva4": {
    "content": "However, it's important to understand that the Metaverse is not a standalone concept. It is a complex ecosystem that requires an integrated network of advanced technologies like Artificial Intelligence (AI)."
  },
  "Diapositiva5": {
    "content": "This joint usage of technology goes under the name of Extended Artificial Intelligence, or XRAI. This research area is gaining prominence because AI plays a vital role in enhancing the immersive nature of the Metaverse. AI models can indeed track objects in real-time, making XR experiences more fluid and realistic. On the other hand, XR is also being adopted by AI researchers to make complex AI models more understandable to the average person."
  },
  "Diapositiva6": {
    "content": "Yet, as this integration progresses and the boundaries between real and virtual continue to blur, we face critical ethical and practical challenges. Chief among them are data privacy and security. The continuous real-time collection of data—often sensitive data—raises significant questions. This data is being gathered from multiple sources, including users, industrial sensors, and even autonomous machines, to feed into XRAI systems. This kind of information flow presents considerable privacy risks and opens doors for potential misuse, particularly in sensitive areas like healthcare or industry, where lives or safety could be online."
  },
  "Diapositiva7": {
    "content": "Given these risks, recent discussions in the technology community have emphasized the need for ethical principles that must guide the development of XRAI. For example, the IEEE Standards Association has initiated global efforts to establish ethical guidelines for XR and related technologies. But despite these efforts, there remains a gap in explicit regulations—especially for emerging spaces like the Metaverse, which increasingly integrate AI into their ecosystems. Our work aims to help close this gap by proposing a comprehensive ethical framework that considers the unique complexities arising from this convergence."
  },
  "Diapositiva8": {
    "content": "This is where our contribution, the XRAI-Ethics Framework, comes into play. The framework we introduce today addresses concerns related to fairness, privacy, bias, accountability, transparency, and responsible use of XRAI technologies in the Metaverse. Our goal is to provide practical guidelines and best practices to ensure that AI is integrated into XR responsibly, ethically, and in a way that maximizes the benefits to society while minimizing harm."
  },
  "Diapositiva9": {
    "content": "One of our main aims with XRAI-Ethics is to examine areas of everyday application where ethical pitfalls are likely to occur. For example, consider the privacy risks associated with virtual medical consultations, where highly sensitive personal information is transmitted over an XR platform. We also suggest ethical principles that can be applied to mitigate these risks."
  },
  "Diapositiva10": {
    "content": "The XRAI Ethics Framework is built on an extensive review of scientific literature, gray literature, and public documents, allowing us to integrate diverse perspectives on ethical concerns. Our approach ensures that the framework is not only comprehensive but also contextually relevant to various stakeholders—including developers, users, and regulatory bodies."
  },
  "Diapositiva11": {
    "content": "The framework itself employs a structured process for extracting, categorizing, and analyzing ethical concerns. We base our work on principles such as transparency, privacy, fairness, and sustainability, ensuring alignment with globally recognized standards like those from UNESCO and IEEE. The purpose is clear: identify the challenges and provide mitigation strategies to ensure that XRAI systems are not only innovative but also ethical and trustworthy."
  },
  "Diapositiva12": {
    "content": "We adapt classical AI ethical principles specifically for XRAI. These principles include:\nTransparency: That transparency is fundamental in building trust. Users must be able to understand how an XRAI system makes decisions, especially in sensitive areas like healthcare and finance. For example, if an AI model is used to diagnose a patient, it’s crucial that both the patient and the healthcare provider understand how the diagnosis was reached. This is where explainability and interpretability come in. The system should be clear enough for users to retain agency over their actions and decisions."
  },
  "Diapositiva13": {
    "content": "Non-Maleficence: This principle indicates that XRAI systems must do no harm—whether physical or psychological. Imagine a scenario in XR gaming where users could be led into dangerous situations due to adversarial attacks. We propose a user-centered approach that emphasizes gradual, evidence-based development of XR technologies that respects user dignity and autonomy while prioritizing safety."
  },
  "Diapositiva14": {
    "content": "Privacy: Privacy is another cornerstone of ethical XRAI. The collection and use of biometric and psychometric data by XRAI systems present significant risks. There is also ambiguity regarding the applicability of existing privacy laws to XR, particularly in public spaces. How do we ensure that surveillance in a virtual public square, for example, aligns with users' privacy expectations? We need robust data protection frameworks to address such concerns."
  },
  "Diapositiva15": {
    "content": "Responsibility and Accountability: XRAI systems must be auditable and traceable. Oversight mechanisms are needed to prevent conflicts with human rights and to ensure the system's environmental and social impacts are monitored. A key debate here is whether accountability lies with the technology itself or its creators. We suggest that all stakeholders—including developers and industry leaders—must commit to ensuring that technology aligns with ethical standards."
  },
  "Diapositiva16": {
    "content": "Sustainability: The issue of sustainability is particularly relevant for XRAI, given the high energy demands of AI models and the added burden of XR technologies, such as remote rendering and blockchain-based NFTs. To create a sustainable future for XRAI, we need to minimize energy consumption and reduce the environmental impact through careful design and interoperability of systems."
  },
  "Diapositiva17": {
    "content": "Fairness: Finally, fairness in XRAI means promoting social justice and ensuring that technology is accessible to all, regardless of background. XR environments must be inclusive and consider the needs of marginalized groups, such as individuals with disabilities. We need to design adaptive mechanisms that can make these technologies equitable, safe, and inclusive for everyone."
  },
  "Diapositiva18": {
    "content": "As we move forward, let's take a closer look at how the XRAI-Ethics framework links ethical principles to specific challenges and provides practical examples of how these principles can be applied effectively. Transparency is essential in XRAI systems to help users understand decisions and processes, building trust and retaining agency. The challenge lies in making complex AI models clear and understandable, especially in XR environments where reasoning can be obscure. For example, In medical XRAI systems, transparency is vital for explaining how AI identifies patterns in diagnostic images, such as detecting tumors or abnormalities. It can also clarify how spatial computing renders patient data in 3D, helping healthcare professionals understand the basis for AI-driven insights. In educational XR platforms, AI systems should transparently explain how they assess student performance and tailor learning experiences, ensuring users can trust the feedback provided. In social XR environments, transparency is critical for explaining how AI monitors behavior, rates interactions, and manages reputation systems, preventing biases and maintaining fairness in social interactions. Additionally, in gaming or virtual workspace settings, transparency can clarify how AI tracks player movements or determines productivity metrics, ensuring users feel informed and in control of their experiences. "
  },
  "Diapositiva19": {
    "content": "To conclude, the XRAI-Ethics framework aims to provide a first form of ethical guidance development of XRAI technologies, ensuring that they align with broader societal goals of fairness, privacy, accountability, transparency, sustainability, and non-maleficence. As we advance these technologies, our goal should always be to put people first, ensuring their safety, their rights, and their ability to thrive in an increasingly connected and immersive digital future.\nThank you all for your attention."
  }
}


if __name__=="__main__":
    audio_dir = "audio/"
    video_clips = []
    for k,v in dict_Diapositivatext.items():
        image_path = f"IDEATE_XR_2024/{k}.PNG" 
        audio_path = f"audio/{k}.mp3" 
        assert os.path.exists(image_path)
        # print(image_path, k,v)
        generate_audio(text=v["content"], filename = audio_path)

        # Load the audio file
        audio = AudioSegment.from_file(audio_path)
        # Get the duration in seconds
        duration_in_seconds = len(audio) / 1000
        print(f"Duration: {duration_in_seconds} seconds")
        
        audio_clip = AudioFileClip(audio_path)

        image_clip = ImageClip(image_path).set_duration(duration_in_seconds)
        image_clip = image_clip.set_audio(audio_clip)

        # Create a list of ImageClips with each image shown for the calculated duration
        video_clips.append(image_clip)
    
    # Concatenate all the ImageClips into a single video
    video = concatenate_videoclips(video_clips, method="compose")


    # Write the result to a video file
    video.write_videofile('slides_video.mp4', fps=24)