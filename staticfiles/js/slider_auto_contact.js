const mediaQuery = window.matchMedia("(prefers-reduced-motion: reduce)");
if (mediaQuery && !mediaQuery.matches) {
	const tagScroller = document.querySelector(".tag-scroller");
	const allTags = tagScroller.querySelectorAll("li");
	
	function createElement(tagName, className = "") {
		const elem = document.createElement(tagName);
		elem.className = className;
		return elem;
	}

	function scrollersFrom(elements, numColumns = 2) {
		const fragment = new DocumentFragment();
		elements.forEach((element, i) => {
			const column = i % numColumns;
			const children = fragment.children;
			if (!children[column]) fragment.appendChild(createElement("ul", "tag-list"));
			children[column].appendChild(element);
		});
		return fragment;
	}
	
	/*	SPLIT THE LIST ELEMENT INTO TWO LISTS
			AND CALL THE ANIMATION
	*/
	const scrollers = scrollersFrom(allTags, 2);
	tagScroller.innerHTML = "";
	tagScroller.appendChild(scrollers);
	addScrolling();

	/*	ADD scrolling CLASS TO THE WRAPPER ELEMENT,
			CLONE EACH LIST ITEM TO MAKE THE LIST LONG ENOUGH
			FOR INFINITE SCROLL AND THEN CALCULATE THE DURATION
			BASED ON WIDTH OF EACH SCROLLER TO MAKE THEM
			MOVE AT THE SAME RATE OF SPEED
			
			DEPENDING ON THE WIDTH OF .tag-scrollers, THE NUMBER OF
			LIST ITEMS AND THEIR INDIVIDUAL WIDTH, YOU MIGHT NEED
			TO CLONE THEM TWO TIMES EACH TO BE SURE EACH .tag-scroller
			WILL BE WIDE ENOUGH TO SUPPORT INFINITE SCROLL
			
			THIS COULD OF COURSE BE ADDED TO THE SCRIPT
			BUT FOR OUR USE CASE, WE KNOW THE MINIMUM NUMBER OF
			LIST ELEMENTS WILL BE ENOUGH FOR ONE CLONE EACH
	*/
	function addScrolling() {
		tagScroller.classList.add("scrolling");
		document.querySelectorAll(".tag-list").forEach((tagList) => {
			const scrollContent = Array.from(tagList.children);
			scrollContent.forEach((listItem) => {
				const clonedItem = listItem.cloneNode(true);
				clonedItem.setAttribute("aria-hidden", true);
				tagList.appendChild(clonedItem);
			});
			tagList.style.setProperty("--duration", (tagList.clientWidth / 100) + "s");
		});
	}
}