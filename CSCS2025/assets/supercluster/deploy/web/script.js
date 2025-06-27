class SuperclusterAPI {
  constructor(baseUrl) {
    this.baseUrl = baseUrl;
  }

  /**
   * Fetches the list of superclusters from the API.
   * @returns {Promise<Array>} A promise that resolves to an array of supercluster objects.
   */
  async getSuperclusterList() {
    try {
      const response = await fetch(`${this.baseUrl}/superclusters/list`);
      if (!response.ok) {
        throw new Error(`Error fetching supercluster list: ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      console.error('Error fetching supercluster list:', error);
      throw error;
    }
  }

  /**
   * Fetches more information about a specific supercluster from the API.
   * @param {string} name The name of the supercluster.
   * @returns {Promise<Object>} A promise that resolves to an object with more information about the supercluster.
   */
  async getSuperclusterInfo(name) {
    try {
      const response = await fetch(`${this.baseUrl}/superclusters/${name}`);
      if (!response.ok) {
        throw new Error(`Error fetching supercluster info: ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      console.error('Error fetching supercluster info:', error);
      throw error;
    }
  }
}

// Create an instance of the SuperclusterAPI class
const api = new SuperclusterAPI('');

// Function to display the list of superclusters
async function displaySuperclusterList() {
  try {
    // Fetch the list of superclusters
    const superclusters = await api.getSuperclusterList();

    // Create a container element for the superclusters
    const superclustersContainer = document.getElementById('superclusters-container');

    // Loop through each supercluster and create a card
    superclusters.forEach(supercluster => {
      const superclusterCard = document.createElement('div');
      superclusterCard.classList.add('supercluster');

      const superclusterHtml = `
        <h2>${supercluster.name}</h2>
        <p>${supercluster.shortDescription}</p>
        <img src="${supercluster.image}" alt="${supercluster.name}">
        <button class="more-info-button" data-name="${supercluster.name}">More Info</button>
      `;

      superclusterCard.innerHTML = superclusterHtml;
      superclustersContainer.appendChild(superclusterCard);
    });

    // Add event listeners to the more info buttons
    const moreInfoButtons = document.querySelectorAll('.more-info-button');
    moreInfoButtons.forEach(button => {
      button.addEventListener('click', async () => {
        const superclusterName = button.getAttribute('data-name');
        const superclusterInfo = await api.getSuperclusterInfo(superclusterName);
        displaySuperclusterInfo(superclusterInfo);
      });
    });
  } catch (error) {
    console.error('Error displaying supercluster list:', error);
  }
}

// Function to display more information about a supercluster
function displaySuperclusterInfo(superclusterInfo) {
  // Create a modal element to display the supercluster info
  const modal = document.createElement('div');
  modal.classList.add('modal');

  const modalHtml = `
    <h2>${superclusterInfo.name}</h2>
    <p>${superclusterInfo.description}</p>
    <ul>
      <li><strong>Number of Galaxies:</strong> ${superclusterInfo.galaxies}</li>
      <li><strong>Distance:</strong> ${superclusterInfo.distance} billion light-years</li>
      <li><strong>Discovery Year:</strong> ${superclusterInfo.discoveryYear}</li>
    </ul>
    <h3>Interesting Facts:</h3>
    <ul>
      ${superclusterInfo.interestingFacts.map(fact => `<li>${fact}</li>`).join('')}
    </ul>
    <button class="close-modal-button">Close</button>
  `;

  modal.innerHTML = modalHtml;
  document.body.appendChild(modal);

  // Add event listener to the close modal button
  const closeModalButton = document.querySelector('.close-modal-button');
  closeModalButton.addEventListener('click', () => {
    modal.remove();
  });
}

// Call the function to display the list of superclusters
displaySuperclusterList();
