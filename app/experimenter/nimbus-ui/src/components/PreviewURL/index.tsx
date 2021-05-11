/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

import React, { useState } from "react";
import Select from "react-select";
import { SelectOption } from "../../hooks/useCommonForm/useCommonFormMethods";
import { StatusCheck } from "../../lib/experiment";
import { getExperiment_experimentBySlug } from "../../types/getExperiment";

type CopyableURLProps = {
  experimentSlug: string;
  branch: string;
  collection: string | boolean;
};

const CopyableURL: React.FC<CopyableURLProps> = ({
  experimentSlug,
  branch,
  collection,
}) => {
  let url = `about:studies?optin_slug=${experimentSlug}&optin_branch=${branch}`;
  const clipboard = navigator.clipboard;
  if (collection) {
    url = `${url}&optin_collection=${collection}`;
  }
  return <code onClick={() => clipboard.writeText(url)}>{url}</code>;
};

export const PreviewURL: React.FC<
  Pick<
    getExperiment_experimentBySlug,
    "slug" | "referenceBranch" | "treatmentBranches"
  > & { status: StatusCheck }
> = ({ slug: experimentSlug, referenceBranch, treatmentBranches, status }) => {
  const [selection, setSelection] = useState(referenceBranch?.slug || "");
  const slugs: SelectOption[] = [];

  if (!referenceBranch || !Array.isArray(treatmentBranches)) {
    return null;
  }

  [referenceBranch.slug, ...treatmentBranches.map((b) => b?.slug)].forEach(
    (branch) => {
      if (branch) {
        slugs.push({ value: branch, label: branch });
      }
    },
  );
  return (
    <>
      <h3 className="h5 mb-3" id="previewURL">
        Preview URL
      </h3>
      <p>
        <b>Click to copy the link</b> and paste it in your browser. You need to
        enable <code>nimbus.debug</code> pref before.
      </p>
      <form data-testid="preview-url-form" className="mb-2">
        <label htmlFor="preview-branch">Selected Branch</label>
        <Select
          onChange={(e) => setSelection(e ? e.value : referenceBranch.slug)}
          defaultValue={slugs[0]}
          options={slugs}
          name="preview-branch"
          inputId="preview-branch"
        />
      </form>
      <p>
        <CopyableURL
          {...{ experimentSlug }}
          branch={selection}
          collection={status.preview && "nimbus-preview"}
        />
      </p>
    </>
  );
};

export default PreviewURL;