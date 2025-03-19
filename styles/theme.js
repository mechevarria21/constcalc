/**
 * Construction Tools - Theme Utilities
 * JavaScript utilities for working with the theme
 */

// Theme configuration
const ConstructionTheme = {
  // Theme colors
  colors: {
    primary: {
      50: '#f0f7ff',
      100: '#e0f0fe',
      200: '#bae0fd',
      300: '#7cc8fb',
      400: '#47a9f5',
      500: '#2c8be8',
      600: '#1a6fd4',
      700: '#1958b2',
      800: '#194992',
      900: '#193f78',
      950: '#102a52'
    },
    secondary: {
      50: '#fffaeb',
      100: '#fef0c7',
      200: '#fee189',
      300: '#fdc94b',
      400: '#fdb022',
      500: '#f59e0b',
      600: '#d97706',
      700: '#b45309',
      800: '#92400e',
      900: '#783610',
      950: '#421c08'
    },
    accent: {
      50: '#f8f8f7',
      100: '#f0efed',
      200: '#e1dfdb',
      300: '#cac7c1',
      400: '#aca7a0',
      500: '#918b83',
      600: '#7c756d',
      700: '#66605a',
      800: '#54504b',
      900: '#46433f',
      950: '#272523'
    },
    neutral: {
      50: '#f9f9f8',
      100: '#f2f2f0',
      200: '#e5e4e1',
      300: '#d2d0cc',
      400: '#aeaba6',
      500: '#8c8982',
      600: '#726e68',
      700: '#5e5b55',
      800: '#4d4a45',
      900: '#413e3a',
      950: '#27251f'
    },
    success: {
      50: '#ecfdf5',
      500: '#10b981',
      700: '#047857'
    },
    warning: {
      50: '#fffbeb',
      500: '#f59e0b',
      700: '#b45309'
    },
    error: {
      50: '#fef2f2',
      500: '#ef4444',
      700: '#b91c1c'
    }
  },

  // Apply theme to dynamic elements
  applyTheme: function() {
    // Apply theme to any dynamically created elements
    document.addEventListener('DOMContentLoaded', function() {
      // Initialize any theme-specific behaviors
      ConstructionTheme.initializeThemeBehaviors();
      
      // Add subtle pattern to hero sections
      ConstructionTheme.enhanceHeroSections();
    });
  },

  // Initialize theme-specific behaviors
  initializeThemeBehaviors: function() {
    // Add active state to navigation links
    ConstructionTheme.highlightActiveNavLink();
    
    // Initialize any calculator result formatting
    ConstructionTheme.initializeCalculatorFormatting();
    
    // Initialize hover effects
    ConstructionTheme.initializeHoverEffects();
  },

  // Highlight the active navigation link based on current URL
  highlightActiveNavLink: function() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav a');
    
    navLinks.forEach(link => {
      const linkPath = link.getAttribute('href');
      if (currentPath === linkPath || 
          (linkPath !== '/' && currentPath.startsWith(linkPath))) {
        link.classList.add('active-nav-link');
        link.style.color = `var(--primary-700)`;
        link.style.fontWeight = 'bold';
      }
    });
  },

  // Format calculator results consistently
  initializeCalculatorFormatting: function() {
    const resultElements = document.querySelectorAll('.calculator-result');
    
    resultElements.forEach(element => {
      // Ensure result values are formatted consistently
      const valueElements = element.querySelectorAll('.result-value');
      valueElements.forEach(valueEl => {
        // Format numbers with 2 decimal places
        if (!isNaN(parseFloat(valueEl.textContent))) {
          valueEl.textContent = parseFloat(valueEl.textContent).toFixed(2);
        }
      });
    });
  },
  
  // Add subtle enhancements to hero sections
  enhanceHeroSections: function() {
    const heroSections = document.querySelectorAll('.hero-section');
    
    heroSections.forEach(section => {
      // Add subtle animation to hero sections
      section.style.transition = 'all 0.3s ease-in-out';
      
      // Add subtle shadow on scroll
      window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
          section.style.boxShadow = '0 15px 30px -10px rgba(0, 0, 0, 0.1)';
        } else {
          section.style.boxShadow = '0 10px 25px -5px rgba(0, 0, 0, 0.08)';
        }
      });
    });
  },
  
  // Initialize hover effects
  initializeHoverEffects: function() {
    // Add hover effects to cards
    const cards = document.querySelectorAll('.feature-card');
    
    cards.forEach(card => {
      card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-8px)';
        this.style.boxShadow = '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)';
        this.style.borderColor = 'var(--primary-200)';
        
        // Find and animate the icon container
        const iconContainer = this.querySelector('.feature-icon-container');
        if (iconContainer) {
          iconContainer.style.transform = 'scale(1.1)';
        }
      });
      
      card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
        this.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03)';
        this.style.borderColor = 'var(--neutral-200)';
        
        // Reset icon container
        const iconContainer = this.querySelector('.feature-icon-container');
        if (iconContainer) {
          iconContainer.style.transform = 'scale(1)';
        }
      });
    });
  },

  // Utility function to get a CSS variable value
  getCssVariable: function(variableName) {
    return getComputedStyle(document.documentElement).getPropertyValue(variableName).trim();
  },

  // Utility function to set a CSS variable
  setCssVariable: function(variableName, value) {
    document.documentElement.style.setProperty(variableName, value);
  },

  // Format a number for display in calculators
  formatNumber: function(number, decimals = 2) {
    return parseFloat(number).toFixed(decimals);
  }
};

// Initialize the theme
ConstructionTheme.applyTheme(); 