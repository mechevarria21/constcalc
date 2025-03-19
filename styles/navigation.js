/**
 * Construction Tools - Navigation Component
 * JavaScript for the navigation component used across pages
 */

document.addEventListener('DOMContentLoaded', function() {
  // Mobile navigation toggle
  const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
  const navLinks = document.querySelector('.nav-links');
  
  if (mobileNavToggle && navLinks) {
    mobileNavToggle.addEventListener('click', function() {
      navLinks.classList.toggle('active');
      
      // Update aria-expanded attribute for accessibility
      const isExpanded = navLinks.classList.contains('active');
      mobileNavToggle.setAttribute('aria-expanded', isExpanded);
    });
  }
  
  // Generate breadcrumbs based on current path
  generateBreadcrumbs();
});

/**
 * Generates breadcrumbs based on the current URL path
 */
function generateBreadcrumbs() {
  const breadcrumbsContainer = document.querySelector('.breadcrumbs');
  if (!breadcrumbsContainer) return;
  
  const currentPath = window.location.pathname;
  const pathSegments = currentPath.split('/').filter(segment => segment !== '');
  
  // Always start with Home
  let breadcrumbsHTML = '<a href="/">Home</a>';
  
  // Build the rest of the breadcrumbs
  let currentPathBuild = '';
  
  pathSegments.forEach((segment, index) => {
    currentPathBuild += `/${segment}`;
    
    // Format the segment for display (capitalize, replace hyphens with spaces)
    const displayName = segment
      .replace(/-/g, ' ')
      .replace(/\b\w/g, char => char.toUpperCase());
    
    if (index === pathSegments.length - 1) {
      // Last segment (current page)
      breadcrumbsHTML += `<span class="separator">/</span><span class="current">${displayName}</span>`;
    } else {
      // Intermediate segments
      breadcrumbsHTML += `<span class="separator">/</span><a href="${currentPathBuild}">${displayName}</a>`;
    }
  });
  
  breadcrumbsContainer.innerHTML = breadcrumbsHTML;
} 