const STATIC_BASE_PATH = "/ltstatic/2026/triennial";

function staticImagePath(folder, file) {
  if (!file) return "";

  const folderPath = folder ? `${folder}/` : "";
  return encodeURI(`${STATIC_BASE_PATH}/${folderPath}${file}`);
}

const partners = [
  "Louisiana Tech University.png",
  "Katho University.png",
  "Jyoti Nivas College.jpg",
  "International Association of Baptist Colleges and Universities.png",
  "Hemophilia Society of Kerala.png",
  "Hansraj College.jpeg",
  "Grambling State University.png",
  "Fergusson College, Pune.jpeg",
  "E- Cure.png",
  "Creating Futures.png",
  "Consortium for Global Education.png",
  "Christ University.png",
  "Christ Nagar College.png",
  "Christ Infotech.png",
  "BVRIT Hyderabad.png",
  "Blue Leaf Impact Solutions.jpg",
  "Binghamton University.png",
  "ACTS Secondary School.png",
  "Actors Collective.jpg",
  "St Francis College for Women.png",
  "Savitribai Phule Pune University.jpg",
  "Project Management Institute, Kerala.png",
  "Presidency University.png",
  "Office of International Affairs.png",
  "NIMHANS.jpg",
  "Nicolaus Copernicus University.png",
  "Mar Ivanios College.jpeg",
  "Loyola Academy.png",
  "Stepping Stones.jpg",
  "Stella Maris Chennai.png",
  "St. Anne_s Degree College for Women.jpeg",
  "St Francis De Sales College.png",
  "University of Szczecin.png",
  "University of Louisiana Monroe.png",
  "University of the Western Cape.jpg",
  "Westlink.png",
  "Women_s Christian college.jpg"
];

if ("scrollRestoration" in history) {
  history.scrollRestoration = "manual";
}

const scrollPositionKey = "ticc:scrollPosition";

function saveScrollPosition() {
  sessionStorage.setItem(scrollPositionKey, JSON.stringify({
    x: window.scrollX,
    y: window.scrollY,
    path: window.location.pathname
  }));
}

function restoreScrollPosition() {
  const saved = sessionStorage.getItem(scrollPositionKey);
  if (!saved) return;

  let position;
  try {
    position = JSON.parse(saved);
  } catch {
    sessionStorage.removeItem(scrollPositionKey);
    return;
  }

  sessionStorage.removeItem(scrollPositionKey);
  if (position.path !== window.location.pathname) return;

  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      const root = document.documentElement;
      const previousScrollBehavior = root.style.scrollBehavior;
      root.style.scrollBehavior = "auto";
      window.scrollTo({
        left: position.x || 0,
        top: position.y || 0,
        behavior: "auto"
      });
      root.style.scrollBehavior = previousScrollBehavior;
    });
  });
}

window.addEventListener("beforeunload", saveScrollPosition);

const coreMembers = [
  { role: "Thematic Area Chair", name: "Dr. Phinu Mary Jose", title: "Administrative Assistant - Watson Institute for Systems Excellence, Binghamton University", email: "phinu.jose@letusdream.org", img: "Dr. Phinu Mary Jose.jpg" },
  { role: "Thematic Area Youth Chair", name: "Ms. Shrushti Mahajan", title: "Youth Lead - Community Conference, Let Us Dream", email: "conference@letusdream.org", img: "Ms. Shrushti Mahajan.jpeg" },
  { role: "Education Convener", name: "Dr. Mini Fernandez", title: "Assistant Professor - Dept of Biotechnology St.Francis College for Women, Begumpet, Hyderabad", email: "minifernandez28@sfc.ac.in", img: "Dr. Mini Fernandez.jpg" },
  { role: "Education International Convener", name: "Ms. Vanelis Rivera", title: "Assistant Professor of English, University of Louisiana Monroe", email: "rivera@ulm.edu", img: "Ms. Vanelis Rivera.jpg" },
  { role: "Health Convener", name: "Susan Abraham Joseph", title: "Er. Susan Joseph : M Tech Dy. Chief Engineer(Retd.), KSEB", email: "susjoseph2000@gmail.com", img: "Susan Abraham Joseph.jpg" },
  { role: "Health International Convener", name: "Ms. Laurie Hall", title: "IABCU Executive Director, International Association of Baptist Colleges and Universities, USA", email: "laurie.hall@baptistschools.org", img: "Ms. Laurie Hall.jpg" },
  { role: "Social Convener", name: "Ms. Srija Santhosh", title: "Consultant - WaSH & ClimateTech, Blue Leaf Impact Solutions, Thiruvananthapuram", email: "sustainabilityues@gmail.com", img: "Ms. Srija Santhosh.jpg" },
  { role: "Social International Convener", name: "Ms. Lauretta Philip", title: "Head of Inclusion and Designated Safeguarding Lead - Westlink International School, Hanoi", email: "laurettaphilip@gmail.com", img: "Ms. Lauretta Philip.jpeg" },
  { role: "Operations 1 - Host University Chair", name: "Dr. Vigneshwaran S A", title: "Assistant Professor - Department of Social Work, CHRIST (Deemed to be University), Bangalore", email: "vigneshwaran.sa@christuniversity.in", img: "Dr. Vigneshwaran S A.jpg" },
  { role: "Host University Operations Co-Chair", name: "Dr. Padmakumar M. M.", title: "Associate Professor, Department of Media Studies CHRIST (Deemed to be University)", email: "", img: "Dr. Padmakumar M. M.png" },
  { role: "Operations 1 - Host University Co-Chair", name: "Dr. Sudha Thomas", title: "Assistant Professor - Department of Social Work CHRIST (Deemed to be University)", email: "sudha.thomas@christuniversity.in", img: "Sudha Thomas.jpg" },
  { role: "Operations 2 - Community Chair", name: "Mr. Rajesh P I", title: "Founder, The Actors Collective", email: "arts.pi@gmail.com", img: "Mr. Rajesh P I.jpg" },
  { role: "Operations 2 - Community Co-Chair", name: "Ms. Suma D", title: "Assistant Professor", email: "sumamerlin98@gmail.com", img: "Ms. Suma D.jpg" },
  { role: "Operations 3 - Organization Chair", name: "Ms. Akhila Gowri Shankar", title: "President, PMI Kerala (Volunteer Role)", email: "president@pmikerala.org", img: "Ms. Akhila Gowri Shankar.png" },  
  { role: "Operations 3 - Organization Co-Chair", name: "Ms. Catherine Namrata", title: "Social Worker", email: "namrathacatherine@gmail.com", img: "Ms. Catherine Namrata.jpg" },  
  { role: "Research Team Lead", name: "Dr. Roseline Florence Gomes", title: "HoD, Department of Psychology, Jyoti Nivas College Autonomous", email: "roseline.gomes@res.christuniversity.in ", img: "Dr. Roseline Gomes.jpeg" },  
  { role: "Research Team Co-Lead", name: "Dr. Anna Tarnowska", title: "Faculty of Law and Administration, Nicolaus Copernicus University in Torun", email: "atarn@law.umk.pl", img: "Dr. Anna Tarnowska.jpg" },  
  { role: "Research Team Co-Lead", name: "Prof. Agnieszka Bien-Kacala", title: "Professor of Constitutional Law - University of Szczecin and Leader of the Research Group: Gender and Constitution in Poland", email: "agnieszka.bien-kacala@usz.edu.pl", img: "Prof. Agnieszka Bien-Kacala.jpg" },
];

const advisoryMembers = [
  { name: "Dr. Fr. Lijo Thomas", title: "Director and Dean, Pune Lavasa Campus, CHRIST (Deemed to be University)", email: "lijo.thomas@christuniversity.in", img: "Fr Lijo.jpeg" },
  { name: "Mr. Jimmy Cherian", title: "Global Lead, LUD Community Conference Founder, Creating Futures", email: "jimmy.cherian@letusdream.org", img: "Jimmy Cherian.jpeg" },
  { name: "Dr. Pauline Leonard", title: "", email: "pauline@letusdream.org", img: "Dr Pauline.jpeg" },
  { name: "Ms. Lisa Jangkamp", title: "Head of International Office - Catholic University of Applied Sciences North Rhine-Westphalia", email: "l.jungkamp@katho-nrw.de", img: "Lisa.jpeg" },
  { name: "Mr. David S R", title: "Founder, E-cure Charitable Trust", email: "david@e-cure.org", img: "David SR.jpg" },
  { name: "Dr. Susanne Mayo", title: "Grambling State University", email: "theussu@gram.edu", img: "Dr Suzanne Mayo.png" },
  { name: "Ms. Divya C", title: "", email: "conference@letusdream.org", img: "Divya C.jpeg" },
  { name: "Ms. Lisa Elam", title: "Louisiana Tech University", email: "lisam@latech.edu", img: "Lisa Elam.jpeg" },
  { name: "Mr. Yogeh L", title: "Global Operation Lead, Let Us Dream", email: "yogesh@letusdream.org", img: "" },
  { name: "Mr. Rohith Fernando", title: "Counsellor - Regional Satellite Centre for Tobacco Quitline Services, Centre for Addiction Medicine (CAM), Dept of Psychiatry, National Institute of Mental Health and Neurosciences (NIMHANS)", email: "rohithfdopsw@gmail.com", img: "" }
];

const testimonials = [
  {
    quote: "I believe LUD in all its splendour can work wonders with its varied and beautifully designed conference. The overall conference can achieve changes in the wider society through youth. As they specify, collaboration and community awareness are some things that will imbibe the spirit of fellowship and growth among youth. With more frequent and more vibrant conferences with international speakers would bring about whirlwinds of change for the better for our nation.",
    preview: "I believe LUD in all its splendour can work wonders with its varied and beautifully designed conference. The overall conference can achieve changes in the wider society through youth. As they specify, collaboration and community awareness",
    name: "Clara M Gerard",
    meta: "Participant, Bangalore"
  },
  {
    quote: "This conference has positively impacted the mindset of many young minds and I feel like it made us realise to become a more responsible citizen and contribute to the social development by helping and uplifting those lower than us and I'm sure that the youth will take necessary steps for the development and empowerment of others as well as themselves.",
    preview: "This conference has positively impacted the mindset of many young minds and I feel like it made us realise to become a more responsible citizen and contribute to the social development",
    name: "Syeda Afiya",
    meta: "Participant, Hyderabad"
  },
  {
    quote: "This conference underscored the power of collaboration and the importance of leading with compassion, empathy, and a clear purpose. The discussions around family engagement, equity, and cross-sector partnerships showed how collective impact can truly transform systems. I was deeply moved by the keynote speakers' focus on \"doing humane work during inhumane times\" and the call to center humanity in our schools, workplaces, and communities. I also appreciated the stories of local changemakers - each one a reminder that small acts of service, when united, create lasting community change.",
    preview: "This conference underscored the power of collaboration and the importance of leading with compassion, empathy, and a clear purpose. The discussions around family engagement, equity, and cross-sector partnerships showed how collective impact can truly transform systems.",
    name: "Jesula Saintus",
    meta: "Participant, USA"
  },
  {
    quote: "There is amazing work being done by so many, but so much more to do! It was great meeting new people and networking with some that I plan to connect with moving forward. Thank you for providing the platform and opportunity.",
    preview: "There is amazing work being done by so many, but so much more to do! It was great meeting new people and networking with some that I plan to connect with moving forward. Thank you for providing the platform and opportunity.",
    name: "Jen Petteys",
    meta: "Participant, USA"
  }
];

function altFromFile(file) {
  return file.replace(/\.[^.]+$/, "").replace(/[_-]/g, " ");
}

function renderPartners() {
  const grid = document.querySelector("#partnersGrid");
  const row1 = document.querySelector("#partnersMarqueeRow1");
  const row2 = document.querySelector("#partnersMarqueeRow2");
  const partnerCard = (file) => `
    <div class="partner-logo-card">
      <img src="${staticImagePath("Our Partners", file)}" alt="${altFromFile(file)}" loading="lazy">
    </div>
  `;

  if (grid) {
    grid.innerHTML = partners.map((file) => `
    <div class="col-6 col-md-4 col-lg-3 col-xl-2">
      <div class="partner-card">
        <img src="${staticImagePath("Our Partners", file)}" alt="${altFromFile(file)}" loading="lazy">
      </div>
    </div>
  `).join("");
  }

  if (row1 && row2) {
    const firstRow = partners.slice(0, 19);
    const secondRow = partners.slice(19, 37);
    row1.innerHTML = [...firstRow, ...firstRow].map(partnerCard).join("");
    row2.innerHTML = [...secondRow, ...secondRow].map(partnerCard).join("");
  }
}

function renderMembers(target, members, folder) {
  const grid = document.querySelector(target);
  if (!grid) return;

  const isCommitteeStyle = target === "#coreGrid" || target === "#advisoryGrid";

  grid.innerHTML = members.map((member) => {
    const email = member.email ? member.email.trim() : "";
    const photo = member.img
      ? `<img class="member-photo" src="${staticImagePath(folder, member.img)}" alt="${member.name}" loading="lazy">`
      : "";

    return `
      <div class="${isCommitteeStyle ? "col-md-6 col-lg-4" : "col-sm-6 col-lg-4 col-xl-3"}">
        <article class="member-card">
          ${isCommitteeStyle && member.role ? `<span class="member-role">${member.role}</span>` : ""}
          ${photo}
          <div class="member-body">
            ${!isCommitteeStyle && member.role ? `<span class="member-role">${member.role}</span>` : ""}
            <h3>${member.name}</h3>
            <p>${member.title}</p>
            ${email ? `<a href="mailto:${email}">${email}</a>` : ""}
          </div>
        </article>
      </div>
    `;
  }).join("");
}

function renderTestimonials() {
  const marquee = document.querySelector("#testimonialsMarquee");
  if (!marquee) return;

  const card = (item, duplicate = false) => {
    const hasMore = item.preview !== item.quote;
    const extra = hasMore ? item.quote.slice(item.preview.length).trim() : "";
    return `
      <article class="testimonial-card"${duplicate ? ' aria-hidden="true"' : ""}>
        <p>
          <span class="testimonial-preview">${item.preview}</span>${hasMore ? `<span class="testimonial-ellipsis"> ... </span><button class="testimonial-more" type="button">see more</button><span class="testimonial-extra"> ${extra}</span>` : ""}
        </p>
        ${hasMore ? `<button class="testimonial-less" type="button">see less</button>` : ""}
        <h3>${item.name}</h3>
        <span>${item.meta}</span>
      </article>
    `;
  };

  marquee.innerHTML = [
    ...testimonials.map((item) => card(item)),
    ...testimonials.map((item) => card(item, true))
  ].join("");

  marquee.addEventListener("click", (event) => {
    const button = event.target.closest(".testimonial-more");
    const lessButton = event.target.closest(".testimonial-less");
    if (!button && !lessButton) return;

    const selectedCard = (button || lessButton).closest(".testimonial-card");
    if (button) {
      selectedCard.classList.add("is-expanded");
      marquee.classList.add("is-paused");
      return;
    }

    selectedCard.classList.remove("is-expanded");
    marquee.classList.remove("is-paused");
  });
}

renderPartners();
renderMembers("#coreGrid", coreMembers, "Core Committee");
renderMembers("#advisoryGrid", advisoryMembers, "Advisory Board Photos");
renderTestimonials();
restoreScrollPosition();